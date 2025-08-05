-- Last updated: 8/5/2025, 2:55:40 PM
# Write your MySQL query statement below
SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING 
    COUNT(timestamp) >= 3;
