-- Last updated: 8/5/2025, 2:53:59 PM
WITH Scores AS 
    (SELECT
        exam_id,
        student_id,
        RANK() OVER (PARTITION BY exam_id ORDER BY score) AS low_score,
        RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS high_score
    FROM
        Exam)

SELECT 
    DISTINCT e.student_id,
    s.student_name
FROM
    Exam e LEFT JOIN Student s USING (student_id)
WHERE
    e.student_id NOT IN
    (SELECT
        student_id
    FROM
        Scores
    WHERE 
        low_score = 1 OR high_score = 1)
ORDER BY
    e.student_id;

