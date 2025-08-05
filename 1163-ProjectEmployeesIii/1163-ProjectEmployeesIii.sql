-- Last updated: 8/5/2025, 2:55:36 PM
# Write your MySQL query statement below
SELECT
    project_id,
    employee_id
FROM
    (SELECT
        project_id,
        employee_id,
        RANK() OVER (PARTITION BY project_id ORDER BY experience_years DESC) AS rnk
    FROM
        Employee JOIN Project USING(employee_id)) AS temp
WHERE
    rnk = 1 




