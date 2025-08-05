-- Last updated: 8/5/2025, 2:55:38 PM
# Write your MySQL query statement below
SELECT
    project_id, 
    (ROUND(AVG(experience_years), 2)) AS average_years
FROM
    Employee e
JOIN 
    Project p
WHERE 
    e.employee_id = p.employee_id
GROUP BY 
    project_id;