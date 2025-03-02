# 🐾 Rescue Animal Dashboard 🐾

## About the Project  
This project is a **dashboard application** that integrates **MongoDB with Dash and Plotly** to provide interactive data visualizations and on-demand analyses. It allows users to **filter, view, and analyze animal shelter data** through:
- An **interactive data table**  
- A **geolocation map**  
- A **donut chart**  

Users can apply **three predefined rescue operation filters** or reset filters to dynamically update the displayed dataset within the visuals. This enables exploration of **breed distributions** while maintaining **CRUD (Create, Read, Update, Delete) operations** securely in the database.

---

## Motivation  
This app simplifies how **Grazioso Salvare** identifies and locates animals for **search-and-rescue training**. This work is **vital** in:  
- Assisting in **locating and rescuing** humans or animals in emergencies  
- **Saving** shelter dogs by giving them a **second chance**  

---

## Exact Versions of Tools Used  

### **For the Dashboard**
| Tool            | Version |
|----------------|---------|
| JupyterDash    | 0.4.2   |
| Dash Leaflet   | 0.1.23  |
| Dash           | 2.8.1   |
| Plotly         | 5.6.0   |
| NumPy          | 1.21.5  |
| Pandas         | 1.4.2   |
| Matplotlib     | 3.5.1   |
| crud.py        | 2.0     |

### **For the CRUD Module**
| Tool            | Version |
|----------------|---------|
| Python         | 3.10.12 |
| MongoDB        | 6.0.13 (Apporto version) |
| PyMongo        | 4.6.1   |
| Jupyter Notebook | 6.4.8 (Apporto version) |

---

## Why These Tools?  
**MongoDB** was chosen for its **flexibility**, unlike rigid SQL schemas, making it ideal for evolving datasets like animal shelters. Its **JSON document structure** integrates well with Python’s **PyMongo**, allowing **efficient CRUD operations**.  

**Dash** acts as both the **viewer and controller** in the MVC setup, enabling:  
- **Interactive web apps** with real-time data updates  
- **Seamless integration** with Plotly for **dynamic visualizations**  
- **User-friendly filtering & UI elements**  

This combination ensures the app is **scalable, responsive, and accessible**.  

---

## Getting Started  
- Install dependencies listed above
    -Example: Pip install pymongo
- Configuring MongoDB Connection
    -Update credentials in the crud.py file
- Run the dashboard from the Jupyter Notebook

---

### **Installation & Configuring MongoDB Connection**  
Ensure all dependencies are installed:  

```bash
pip install pymongo dash plotly numpy pandas matplotlib
```

Update MongoDB credentials in crud.py

---

## Usage
- Run all cells and then click the link that is returned
![image](https://github.com/user-attachments/assets/f97b9322-c01c-466e-8556-d3cb2c50d9c3)
- The dashboard is defaulted to the preset filter option ‘Reset Filters’ to show no filters as shown below:
![image](https://github.com/user-attachments/assets/801771e7-4445-4867-acb3-a4a21e059e1d)
- There are three other preset filter options to help focus in on the best breeds and other factors for specific rescue operations. Below is an Example for 'Water Rescue'.
  ![image](https://github.com/user-attachments/assets/d2569385-3dcb-4a98-9697-20a694e6a33f)
- In addition to these preset filters, users can choose specific filtering and sorting options.

  ![image](https://github.com/user-attachments/assets/72518293-42fd-46fe-952c-0d97d1349629)
  ![image](https://github.com/user-attachments/assets/5906a7c8-39f0-434e-b234-dd95a387e1f6)

In the individual CRUD Module you can create, read, update and delete records as shown below.
- Creating a new record can be done by using crud.create(data to enter)
  
  ![image](https://github.com/user-attachments/assets/c9863c77-5449-4686-adce-0a1498a2dd47)
- Searching for an existing record
  
  ![image](https://github.com/user-attachments/assets/1e1430a1-50e1-418c-8d61-bba2c3899cab)

---

## Code Example
Below is an example of the dashboard code that sets the suggested filter options at the top left of the dashboard:
![image](https://github.com/user-attachments/assets/eea0257b-feb0-4583-99c2-ac3a01e3ce64)
![image](https://github.com/user-attachments/assets/b36d45fd-0881-4950-a2be-0c780fd95486)

And the below shows how the donut chart, using Plotly, was designed to show the distribution of breeds and the total number of dogs based on the filter selected as well as handling the data labels when there was a large number of results:

  ![image](https://github.com/user-attachments/assets/0f5f2c73-5c2b-4900-9e34-6dee0aef0818)
  ![image](https://github.com/user-attachments/assets/5f3715aa-cdc4-4854-84f8-a1654ab31d65)

Below is an example of a user creating a new record for a Siamese Cat via crud.create() and then searching all records via crud.read():

  ![image](https://github.com/user-attachments/assets/0f01a89c-ff22-4648-8590-87a65fa1d009)

---

## Tests
You can test that you can successfully create a new record by running CRUD Testing.ipynb or manually running your own tests similar to:
- Code: crud.create(create_test)
  - Expected Output: ‘Data created!’ confirmation
- Code: crud.read(read_test)
  - Expected Output: query results if a match was found, else an exception.
![image](https://github.com/user-attachments/assets/a0f073ec-00ca-48e7-a980-9624866dd4eb)
![image](https://github.com/user-attachments/assets/f67e594d-c00d-46b1-b99f-32a6d46d278b)
![image](https://github.com/user-attachments/assets/c90d0103-0a5d-4cac-a263-79bffb5f7d3c)
![image](https://github.com/user-attachments/assets/d1913358-2c1f-4182-918b-3391749c692c)

---

## Contact
Your name: Audrey Weaver, audrey.weaver@snhu.edu


