-- Last updated: 8/5/2025, 2:53:02 PM
# Write your MySQL query statement below
SELECT 
    user_id, 
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM 
    Users
ORDER BY 
    user_id;