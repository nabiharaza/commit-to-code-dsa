-- Last updated: 8/5/2025, 2:53:42 PM
# Write your MySQL query statement below
SELECT
    product_name,
    product_id,
    order_id,
    order_date
FROM
    Products
    JOIN Orders USING(product_id)
WHERE
    (product_id,order_date) IN
    (SELECT
        product_id,
        MAX(order_date)
    FROM
        Orders
    GROUP BY
        product_id)
ORDER BY
    product_name,
    product_id,
    order_id;