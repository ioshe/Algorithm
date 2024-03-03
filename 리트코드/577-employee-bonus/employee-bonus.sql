# Write your MySQL query statement below
select 
    name,
    bonus
from
    Employee 
LEFT Join
    Bonus
ON
    Employee.empId = Bonus.empId
Where
    bonus < 1000 OR bonus IS NULL
