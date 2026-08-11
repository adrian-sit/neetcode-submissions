-- Write your query below
SELECT a.student_id, MIN(exam_id) AS exam_id, score
FROM exam_results a
JOIN (
    SELECT student_id, MAX(score) AS max_score
    FROM exam_results
    GROUP BY student_id
) b
ON a.student_id = b.student_id
AND a.score = b.max_score
GROUP BY a.student_id, a.score
ORDER BY a.student_id ASC
