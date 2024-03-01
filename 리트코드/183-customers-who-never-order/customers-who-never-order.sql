# Write your MySQL query statement below
select name as Customers
from Customers As C
LEFT Join Orders AS O
On C.id = O.customerId 
where customerId is null