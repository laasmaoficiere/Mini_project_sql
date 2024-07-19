
# Importing the required libraries
import pandas as pd
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#Connecting to the MySQL database
user = "root"
password = "new_password"
host = "127.0.0.1"
port = "3306"
db = "Project_2"
from sqlalchemy import create_engine
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}')

# This function is used to import the first query from the database
# This query is used to find the total quantity of products sold by product name and product type for different age groups
def hypo_1():
    query_1 = """
    SELECT
        CASE
            WHEN age BETWEEN 18 AND 35 THEN '18-35'
            WHEN age > 35 THEN '35+'
            ELSE 'Other'
        END AS age_group,
        product_type,
        product_name,
        SUM(quantity) AS total_quantity
    FROM (
        SELECT
            customers.customer_id,
            customers.age,
            orders.order_id,
            sales.product_id,
            sales.quantity,
            products.product_name,
            products.product_type
        FROM customers
        JOIN orders ON customers.customer_id = orders.customer_id
        JOIN sales ON orders.order_id = sales.order_id
        JOIN products ON sales.product_id = products.product_id
    ) AS subquery
    GROUP BY age_group, product_type, product_name
    ORDER BY age_group, product_type;
    """
    df_1 = pd.read_sql(query_1, con=engine)
    return df_1



# This function is used to import the second query from the database
# This query is used to find the total quantity of products sold per gender and colour
def hypo_2():
    query_2 = """
    SELECT
        gender,
        colour,
        SUM(quantity) AS total_quantity
    FROM (
        SELECT
            customers.customer_id,
            customers.gender,
            orders.order_id,
            sales.product_id,
            sales.quantity,
            products.colour
        FROM customers
        JOIN orders ON customers.customer_id = orders.customer_id
        JOIN sales ON orders.order_id = sales.order_id
        JOIN products ON sales.product_id = products.product_id
    ) AS subquery
    GROUP BY gender, colour
    ORDER BY gender, colour;
    """

    df_2 = pd.read_sql(query_2, con=engine)
    return df_2

# This function is used to import the third query from the database
# This query is used to find the minimum, maximum, and average price of products sold by product category
def hypo_3():
    query_3 = """
    SELECT
        product_type,
        MIN(price) AS min_price,
        MAX(price) AS max_price,
        AVG(price) AS mean_price
    FROM
        products
    GROUP BY
        product_type
    ORDER BY
        product_type;
    """

    df_3 = pd.read_sql(query_3, con=engine)
    return df_3


# This function is used to visualise the data from the first query
# It creates a bar chart to show the total quantity of products sold by product name and product type
def visualize_bar(df_1):
    fig_bar = px.bar(df_1, x='product_name', y='total_quantity', color='product_type', 
                     title='Total Quantity by Product Name and Product Type',
                     labels={'total_quantity':'Total Quantity', 'product_name':'Product Name'})
    fig_bar.show()


# This function is used to visualise the data from the first query
# It creates a scatter plot to show the total quantity of products sold by product name and product type for different age groups
def visualize_scatter(df_1):
    fig = px.scatter(df_1, x='product_name', y='total_quantity', color='product_type', symbol='age_group',
                 title='Total Quantity by Product Name, Product Type, and Age Group',
                 labels={'product_name': 'Product Name', 'total_quantity': 'Total Quantity'})

    fig.update_layout(
    xaxis_title='Product Name',
    yaxis_title='Total Quantity'
    )

    fig.update_traces(marker=dict(size=12,  # Marker size
                               line=dict(width=2, color='DarkSlateGrey')),  # Marker border settings
                  selector=dict(mode='markers')) 

    fig.show()    

# This function is used to visualise the data from the first query
# It creates a treemap to show the distribution of product type and product type
def visualize_tree(df_1):
    fig_treemap = px.treemap(df_1, path=['product_type', 'product_name'], values='total_quantity', 
                         title='Product Type and Product Name Distribution')
    fig_treemap.show()

# This function is used to visualise the data from the second query
# It creates a scatter plot to show the total quantity of colours sold based on gener
def visualize_scatter1(df_2):
    custom_colors = {
    'red': 'rgb(255, 0, 0)',
    'blue': 'rgb(0, 0, 255)',
    'green': 'rgb(0, 128, 0)',
    'orange': 'rgb(255, 165, 0)',
    'indigo': 'rgb(75, 0, 130)',
    'violet': 'rgb(238, 130, 238)',
    'yellow': 'rgb(255, 255, 0)'
}

# Scatter plot with custom colors
    fig_scatter = px.scatter(df_2, x='gender', y='total_quantity', color='colour', size='total_quantity',
                         title='Total Quantity by Gender and Colour',
                         color_discrete_map=custom_colors)

# Update layout
    fig_scatter.update_layout(
    xaxis_title='Gender',
    yaxis_title='Total Quantity'
)

# Show plot
    fig_scatter.show()    
    










