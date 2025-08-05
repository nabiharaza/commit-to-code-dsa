-- Last updated: 8/5/2025, 2:53:39 PM
# Write your MySQL query statement below
SELECT
    name AS warehouse_name,
    SUM(w.units * p.Width * p.Length * p.Height) AS volume
FROM
    Warehouse w
    LEFT JOIN Products p
ON
    w.product_id = p.product_id
GROUP BY
    w.name;
