# Write your MySQL query statement below
select class
from Courses
Group by class
having count(student)>=5