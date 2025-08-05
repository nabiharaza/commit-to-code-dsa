-- Last updated: 8/5/2025, 2:53:36 PM
# Write your MySQL query statement below
SELECT
    customer_id,
    product_id,
    product_name
FROM
    (SELECT
        *,
        RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(product_id) DESC) AS rnk
    FROM
        Orders JOIN Products USING(product_id)
    GROUP BY
        customer_id,
        product_id) AS temp
WHERE
    rnk = 1



