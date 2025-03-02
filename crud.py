from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user= "aacuser", password="SNHU1234", host="nv-desktop-services.apporto.com",
                 port = 31319, db="AAC", col="animals"):
        # Initializing the MongoClient
        
        # Connection Variables
        # Using the user account I created last week with same creds
#         USER = 'aacuser'
#         PASS = 'SNHU1234'
#         HOST = 'nv-desktop-services.apporto.com'
#         PORT =  31319 # 31580
#         DB   = 'AAC'  #'aac' -is all caps in show dbs
#         COL  = 'animals'
    
        # Initialize Connection
        #self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        #self.database = self.client['%s' % (DB)]
        #self.collection = self.database['%s' % (COL)]
        # 2/14 update
        self.client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
        self.database = self.client[db]
        self.collection = self.database[col]

#   helper function for creation, setting ids
#   unable to use _id field since it is not a numerical that is able to be 
#   incremented here so rec_num as suggested is created
    def getNextRecordNum(self):
#         returns the next available record number
        
        try:  # to find the document with the highest #
            latest_record = self.collection.find_one( {},  
                sort=[("rec_num", -1)]  #sort descending
            )

            # asssings new record number, since sorted desc this would be the true next additional number
            if latest_record and "rec_num" in latest_record:
                return latest_record["rec_num"] + 1 
            else:
                return 1  

        except Exception as e:
            print("Error retrieving the next record number: " + {e}) # prints exception info
            return None 

    
    # Complete this create method to implement the C in CRUD. Original for backup
#     def create(self, data):
#         # if data exists
#         if data is not None:
#             self.database.animals.insert_one(data)  # data should be dictionary   
#             print("Data created!")
#         else:
#             # no data found given the connection variables, raise exception
#             raise Exception("Nothing to save, because data parameter is empty")
            
    # Complete this create method to implement the C in CRUD.
    # updated based on feedback from last module (no notes, code block only)
    def create(self, data):
        print("Creation in progress...")
        # if data exists
        if data is None or not isinstance(data, dict):
            raise ValueError("Invalid input: data must be a dictionary.")

        try:
            # generate the new record number that is next in line
            index_num = self.getNextRecordNum()

            # Debug statement
            print("Successfully generated the Record # :", index_num)

            # add unique record number
            data["rec_num"] = index_num

            # insert into database
            ret = self.collection.insert_one(data)

            # Check if creation was successful
            if ret.inserted_id:
                return True  
            else:
                return False 

        except Exception as e:
            print(f"Error inserting record: {e}")  # Log the error
            return False

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            # return list of reuslts from search using find() so it can return multiple results
            cursor = self.collection.find(data)
            return list(cursor)
        else:
            #return no data specified to find
            raise Exception("Data not found")
     
    # Function for updating one or multiple existing records
    # if multiple it must be specified, else false and defaults to updating one record
    def update(self, query, update_values, multiple=False): 
        if query is None or not isinstance(query, dict):
            raise ValueError("Invalid input: data must be a dictionary.")

        if update_values is None or not isinstance(update_values, dict):
            raise ValueError("Invalid input: data must be a dictionary.")
        
        # try/catch exception to help with debbugging 
        try:
            update_type = {"$set": update_values}  # use MongoDB's syntax to set new values

            if multiple: #if 4th arg was set to true then it should update multiple
                result = self.collection.update_many(query, update_type)
            else: #updates only 1 record
                result = self.collection.update_one(query, update_type)
            
            # return # of docs udpated
            return print("Records updated: " + str(result.modified_count)) or result.modified_count
            
        except Exception as e:
            print("Error updating record(s): " + {e}) or 0
            return 0  # return none updated
        
    # function for deleting one or multiple docs based on query passed         
    def delete(self, query, multiple=False):
        if query is None or not isinstance(query, dict):
            raise ValueError("Invalid input: query must be a disctionary")
            
        # try/catch exception to help with debbugging    
        try: 
            if multiple: #if 3rd arg was set to true then it should delete multiple
                result = self.collection.delete_many(query)
            else: # deletes only 1 record
                result = self.collection.delete_one(query)
             
            return print("Records deleted: " + str(result.deleted_count)) or result.deleted_count
        
        except Exception as e:
            return print("Error deleting record(s): " + {e}) or 0
        
            