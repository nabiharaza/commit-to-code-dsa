-- Last updated: 8/5/2025, 2:54:02 PM
SELECT 
    c.customer_id AS customer_id,
    c.customer_name AS customer_name
FROM
    Customers c
LEFT JOIN
    Orders o
ON
    c.customer_id = o.customer_id 
GROUP BY
    c.customer_id
HAVING
    SUM(o.product_name = 'A') > 0
    AND SUM(o.product_name = 'B') > 0
    AND SUM(o.product_name = 'C') = 0
ORDER BY
    c.customer_id;