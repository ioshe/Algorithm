# Write your MySQL query statement below
select 
    Prices.product_id,
    ifnull(round(sum(price * units) / sum(units),2),0) as average_price
From Prices
LEFT JOIN UnitsSold
On
    Prices.product_id = UnitsSold.product_id
    AND UnitsSold.purchase_date Between start_date and end_date
group by
    product_id
    