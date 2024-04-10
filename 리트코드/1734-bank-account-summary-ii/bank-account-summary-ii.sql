# Write your MySQL query statement below
select
    name
    , sum(amount) as balance
from Transactions JOIN Users ON Transactions.account = Users.account
group by Transactions.account
HAVING sum(amount) > 10000