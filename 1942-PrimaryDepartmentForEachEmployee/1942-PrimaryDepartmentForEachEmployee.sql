-- Last updated: 8/5/2025, 2:52:44 PM
# Write your MySQL query statement below
SELECT
    employee_id,
    department_id
FROM
    Employee
WHERE
    primary_flag = 'Y'
UNION
SELECT
    employee_id,
    department_id
FROM
    Employee
GROUP BY
    employee_id
HAVING 
    count(employee_id) = 1;