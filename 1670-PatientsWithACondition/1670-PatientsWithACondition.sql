-- Last updated: 8/5/2025, 2:53:44 PM
# Write your MySQL query statement below
SELECT
    patient_id, 
    patient_name, 
    conditions
FROM
    Patients
WHERE
    conditions REGEXP '(^| )DIAB1';