-- Last updated: 8/5/2025, 2:53:47 PM
# Write your MySQL query statement below
SELECT 
    c.name AS country
FROM
    Country c
JOIN 
    Person p ON substring(p.phone_number, 1, 3) = c.country_code
JOIN 
    Calls ca ON p.id IN (ca.caller_id, ca.callee_id)
GROUP BY
    c.name
HAVING 
    AVG(duration) > (SELECT AVG(duration) FROM Calls);
 
