USE Project_2;
select * from products;
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