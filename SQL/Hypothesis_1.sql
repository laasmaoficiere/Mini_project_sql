USE Project_2;
-- CREATE TABLE customer_age_product1 AS

SELECT
    CASE
        WHEN age BETWEEN 18 AND 35 THEN '18-35'
        WHEN age > 35 THEN '35+'
        ELSE 'Other'
    END AS age_group,
    product_type,product_name,
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
        
    FROM
        customers
    JOIN
        orders ON customers.customer_id = orders.customer_id
    JOIN
        sales ON orders.order_id = sales.order_id
    JOIN
        products ON sales.product_id = products.product_id
) AS subquery
GROUP BY
    age_group, product_type, product_name
ORDER BY
    age_group, product_type;

    

    
    
    


  
    