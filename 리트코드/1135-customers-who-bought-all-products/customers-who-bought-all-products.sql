# Write your MySQL query statement below
select 
    customer_id
from
    Product p
LEFT JOIN Customer c ON p.product_key = c.product_key
GROUP BY c.customer_id
HAVING COUNT(distinct(p.product_key)) = (SELECT COUNT(product_key) FROM Product);