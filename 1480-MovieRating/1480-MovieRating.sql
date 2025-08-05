-- Last updated: 8/5/2025, 2:54:10 PM
# Write your MySQL query statement below
(SELECT
    u.name AS results
FROM
    Users u JOIN
    MovieRating m
USING
    (user_id)
GROUP BY
    u.name
ORDER BY
    COUNT(*) DESC, u.name LIMIT 1)
    
UNION ALL

(SELECT
    mo.title AS results
FROM
    Movies mo JOIN
    MovieRating m
USING
    (movie_id)
WHERE
    m.created_at LIKE '2020-02%'
GROUP BY
    mo.title
ORDER BY
    AVG(m.rating) DESC, mo.title LIMIT 1);