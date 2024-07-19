USE Project_2;
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
    gender, colour
ORDER BY
    gender, colour;






    

    
    
    


  
    