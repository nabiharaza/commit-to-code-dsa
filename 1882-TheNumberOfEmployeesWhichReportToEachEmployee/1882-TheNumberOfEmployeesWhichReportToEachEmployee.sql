-- Last updated: 8/5/2025, 2:52:56 PM
-- # Write your MySQL query statement below
SELECT 
   reports_to as employee_id,
   (
    SELECT
        name
    FROM
        employees e1
    WHERE
        e.reports_to = e1.employee_id) as name,
   COUNT(reports_to) as reports_count,
   ROUND(AVG(age)) AS average_age
FROM
    employees e
GROUP BY
    reports_to
HAVING 
    reports_count > 0
ORDER BY
    employee_id;
