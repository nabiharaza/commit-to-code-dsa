-- Last updated: 8/5/2025, 2:54:16 PM
# Write your MySQL query statement below
SELECT
    employee_id,
    COUNT(team_id) OVER(PARTITION BY team_id) AS team_size
FROM
    Employee;