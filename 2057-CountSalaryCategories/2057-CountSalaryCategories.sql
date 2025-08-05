-- Last updated: 8/5/2025, 2:52:37 PM
# Write your MySQL query statement below
SELECT
    'Low Salary' AS category,
    (SELECT COUNT(*) FROM Accounts a WHERE a.income < '20000') AS accounts_count
    
UNION

SELECT
    'Average Salary' AS category,
    (SELECT COUNT(*) FROM Accounts a WHERE a.income >= '20000' AND a.income <= '50000') AS accounts_count

UNION

SELECT
    'High Salary' AS category,
    (SELECT COUNT(*) FROM Accounts a WHERE a.income > '50000') AS accounts_count;