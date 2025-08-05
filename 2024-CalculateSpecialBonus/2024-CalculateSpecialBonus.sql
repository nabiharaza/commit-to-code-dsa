-- Last updated: 8/5/2025, 2:52:40 PM
# Write your MySQL query statement below
SELECT
    employee_id,
    IF(employee_id % 2 = 1 AND name NOT REGEXP '^M', salary, 0) AS bonus
FROM
    Employees
ORDER BY
    employee_id;