-- Last updated: 8/5/2025, 2:54:28 PM
# Write your MySQL query statement below
WITH temp AS 
(SELECT
    fail_date AS day,
    'failed' AS period_state,
    DAYOFYEAR(fail_date) - row_number() over(ORDER BY fail_date) as period_group 
FROM
    Failed
WHERE
    fail_date BETWEEN '2019-01-01' AND '2019-12-31'
UNION ALL
SELECT
    success_date AS day,
    'succeeded' AS period_state,
    DAYOFYEAR(success_date) - row_number() over(ORDER BY success_date) as period_group 
FROM
    Succeeded
WHERE
    success_date BETWEEN '2019-01-01' AND '2019-12-31')


SELECT
    period_state,
    MIN(day) AS start_date,
    MAX(day) AS end_date
FROM
    temp
GROUP BY
    period_state,
    period_group
ORDER BY
    start_date