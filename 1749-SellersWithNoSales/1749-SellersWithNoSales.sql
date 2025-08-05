-- Last updated: 8/5/2025, 2:53:38 PM
# Write your MySQL query statement below
SELECT
    seller_name
FROM
    Seller s
LEFT JOIN 
    Orders o
ON
    o.seller_id = s.seller_id
GROUP BY
    s.seller_id
HAVING
    SUM(IFNULL(YEAR(o.sale_date) = 2020, 0)) < 1
ORDER BY
    s.seller_name;
    