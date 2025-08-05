-- Last updated: 8/5/2025, 2:53:45 PM
# Write your MySQL query statement below
SELECT
    user_id,
    name,
    mail 
FROM
    Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$';