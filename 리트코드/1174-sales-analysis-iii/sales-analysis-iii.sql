# Write your MySQL query statement below
-- select
--     product_id
--     , product_name
-- from 
--     Product
-- where
--     product_id in (
--         select product_id
--         from Sales
--         where sale_date BETWEEN '2019-01-01' AND '2019-03-31'
--     )
--     and 
--     product_id not in (
--         select product_id
--         from Sales
--         where sale_date < '2019-01-01' OR sale_date > '2019-03-31'
--     )

select 
    Product.product_id
    , product_name
from
    Product LEFT JOIN Sales
ON 
    Product.product_id = Sales.product_id
group by Product.product_id
HAVING
    min(sale_date) >= '2019-01-01'
    AND max(sale_date) <= '2019-03-31'

