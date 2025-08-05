-- Last updated: 8/5/2025, 2:53:51 PM
# Write your MySQL query statement below
SELECT
    sell_date,
    count(DISTINCT product) as num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') as products
FROM
    Activities
GROUP BY
    sell_date
ORDER BY
    sell_date;