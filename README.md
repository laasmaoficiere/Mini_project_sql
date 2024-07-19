
## Business problem

Luxury fashion retailer wants to better manage their stock and promotions, therefore the business needs help with understanding their current customer behaviour to make data driven decisions. 


## Project Overview

Fashion retailer needs help with understanding their current customer behaviour to make data driven stock and promotion decisions. This analysis determines the current customer trends in style, colour and product choice based on customer age and gender.



## Example beneficiaries of this data analysis include

We have collected data from kaggle and extracted 4 different datasheets containing primarily customer details, customer orders, products and sales. Each table contains description of products eg, product names, product type, customer gender, customer age, price, total quantity.

## ERM
<img width="687" alt="Screenshot 2024-07-19 at 08 25 45" src="https://github.com/user-attachments/assets/18de1eae-939a-43bc-a732-6af117736ba6">



## :question:`Hypothesis
The hypothesis will help us uncover insights that address the problem statement and provide analysis based on the available datasets.


### **EDA - 1️ Hypothesis**
1.Certain styles in each product category are more popular than others, highlighting a current trend.
**Tables used:**

- sales(total_quantity);
- products(product_name, product_type);
- customers(age_group).
![hypo1](https://github.com/user-attachments/assets/3036219a-b052-4580-bee3-4033f37b9c02)




### **EDA - 2 Hypothesis**
2.The demand for certain styles differs between customers aged 18-35 and customers above the age of 35
**Tables used:**

- orders(quantity);
- products(colour, product_type);
- customers(age_group).
![hypo_2](https://github.com/user-attachments/assets/761f9e15-e52d-4f62-ac97-2de4e0fbba0d)

  
  
### **EDA - 3 Hypothesis**
3.There is a distinct difference in colour preference based on the gender of customers.

- orders(quantity);
- products(colour, product_type);
- customers(gender).
![scatter_hyp_2](https://github.com/user-attachments/assets/1ad63e60-7676-40bb-ad93-b3abca7bb006)

  
   

## Milestones

  1. Project Preparation-Organize the project team-Create Notion board
     
  2. Define problem statement-Identify Business Question
  3. Code Review and Testing-Review code from Local and Dev branches-Once reviewed and approved, merge 
     into Main branch
  4. Presentation
  

## :toolbox: Tools and Technologies Used

- Mysql workbench: We created the Entity-Relationship Model, followed by data transformation processing steps. These steps involved merging, grouping, and cleaning all datasets, and filtering the data to best test our hypothesis through MySQL.
- Python: The main programming language used for data visualization.
- Jupyter Notebook: Used for data visualization and addressing the project questions.
- Plotly python graphing library

## Project Structure

The project structure is as follows:

- `notebooks/main.py`: The Jupyter Notebook containing the data processing, analysis, and visualization code.
- data.sql: SQL files containing all proceesed data and information.
- `data/`: A folder containing the dataset files obtained from the IEA.
- `app/`: A folder containing the application code for creating the project dashboard.
- `requirements.txt`: A file specifying the dependencies required to run the project.


## Conclusion
Our hypothesis confirmed that there are differences in style and product preferences based on age and gender. These insights can assist the business in targeting promotional activities, capitalizing on current trends, and improving stock management. However, since this is synthetic data, it serves well for the technical aspects of the project but lacks significant value for real-world analysis. Utilizing MySQL and Python in this project demonstrates their effectiveness, and the approach could be expanded to handle larger, more complex datasets. This would enable the creation of more advanced queries or the integration of additional data for enhanced analysis.




### Link
https://www.kaggle.com/datasets/ruchi798/shopping-cart-database
  
