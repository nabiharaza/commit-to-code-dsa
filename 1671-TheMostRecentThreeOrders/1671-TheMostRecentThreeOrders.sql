-- Last updated: 8/5/2025, 2:53:43 PM
# Write your MySQL query statement below
SELECT
    customer_name, 
    customer_id, 
    order_id, 
    order_date
FROM
    (SELECT
        c.name AS customer_name,
        o.customer_id,
        o.order_id,
        o.order_date,
        RANK() OVER (PARTITION BY c.customer_id ORDER BY order_date desc) AS rnk
    FROM
        Orders o
    JOIN
        Customers c USING(customer_id)) as Temp
WHERE 
    rnk <= 3
ORDER BY
    customer_name,
    customer_id,
    order_date DESC;
    
  