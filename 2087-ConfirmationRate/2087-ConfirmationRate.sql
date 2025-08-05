-- Last updated: 8/5/2025, 2:52:34 PM
# Write your MySQL query statement below
SELECT 
    s.user_id,
    ROUND(AVG(IF(c.action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM
    Signups AS s LEFT JOIN
    Confirmations AS c
ON
    c.user_id = s.user_id
GROUP BY
    user_id;
