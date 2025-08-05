-- Last updated: 8/5/2025, 2:52:56 PM
# Write your MySQL query statement below
SELECT
    user_id,
    count(follower_id) as followers_count
FROM
    Followers
GROUP BY
    user_id
ORDER BY
    user_id;