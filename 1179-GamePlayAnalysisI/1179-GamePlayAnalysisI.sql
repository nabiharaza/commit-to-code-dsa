-- Last updated: 8/5/2025, 2:55:03 PM
# Write your MySQL query statement below
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM
    Activity
GROUP BY
    player_id;
