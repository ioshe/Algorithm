# Write your MySQL query statement below
with top_sal_view as (
    select 
        max(salary) as top_salary
        , Employee.departmentId
        , Department.name
    from Employee join Department
    ON Employee.departmentId = Department.id
    group by
        departmentId
)

select 
    t.name as Department
    , E.name as Employee
    , E.salary as Salary
from Employee E join top_sal_view t 
ON  E.departmentId = t.departmentId
where E.salary = t.top_salary