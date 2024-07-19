USE Project_2;
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    home_address VARCHAR(255),
    zip_code VARCHAR(20),
    city VARCHAR(50),
    State VARCHAR(50),
    country VARCHAR(50)
);
CREATE TABLE products (
    product_ID INT AUTO_INCREMENT PRIMARY KEY,
    product_type VARCHAR(50),
    product_name VARCHAR(50),
    size VARCHAR(10),
    colour VARCHAR(20),
    price INT,
    quantity INT,
    description VARCHAR(200)
    
);
CREATE TABLE sales (
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
	order_id INT,
    product_id INT,
    price_per_unit INT,
    quantity INT,
    total_price INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    
);
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    payment INT,
    order_date DATE,
    delivery_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
   
);