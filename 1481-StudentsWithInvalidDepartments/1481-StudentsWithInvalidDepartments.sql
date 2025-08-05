-- Last updated: 8/5/2025, 2:54:09 PM
# Write your MySQL query statement below
SELECT
    id,
    name
FROM
    Students
WHERE
    department_id NOT IN 
    (SELECT
        id
    FROM
        Departments);