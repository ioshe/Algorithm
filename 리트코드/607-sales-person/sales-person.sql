# Write your MySQL query statement below
with red_id as (
    select sales_id
    from Orders
    where com_id = (
        select com_id
        from Company
        where name = "RED"
    )
)

select name
from SalesPerson
where sales_id not in (select sales_id from red_id ) 