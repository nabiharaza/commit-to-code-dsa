-- Last updated: 8/5/2025, 2:53:37 PM
# Write your MySQL query statement below
SELECT
    u.name,
    (SUM(t.amount)) AS balance
FROM
    Transactions t 
    JOIN Users u
ON
    u.account = t.account
GROUP BY
    u.account
HAVING 
    balance > 10000;