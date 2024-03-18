# Write your MySQL query statement below
select 
    project_id
    , ROUND(AVG(experience_years),2) as average_years
from
    Project
JOIN
    Employee
ON
    Project.employee_id = Employee.employee_id
GROUP BY
    project_id