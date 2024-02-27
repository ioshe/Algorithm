# Write your MySQL query statement below
select 
    firstName, 
    lastName, 
    city,
    state
from Address
right join Person
on Address.personId = Person.personId