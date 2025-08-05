-- Last updated: 8/5/2025, 2:52:25 PM
# Write your MySQL query statement below


-- teacherid   subid   deptid
-- 1           1       3
-- 1           2`      3
-- 1           2       4
-- 2           2       4

-- 0/p :----
-- 1   2
-- 2   1

SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) as cnt
FROM
    Teacher t
GROUP BY
    teacher_id;
