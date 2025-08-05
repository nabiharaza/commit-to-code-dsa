-- Last updated: 8/5/2025, 2:52:35 PM
SELECT
    employee_id
FROM
    Employees
WHERE 
    employee_id NOT IN
    (SELECT
        employee_id
    FROM
        Salaries)
UNION
SELECT
    employee_id
FROM
    Salaries
WHERE 
    employee_id NOT IN
    (SELECT
        employee_id
    FROM
        Employees)
ORDER BY
    employee_id;
    