select 
    date_format(os.sales_date, '%Y-%m-%d') sales_date,
    os.product_id,
    os.user_id,
    os.sales_amount
from (
    select 
        sales_date,
        product_id,
        user_id,
        sales_amount from online_sale
    union all
    select 
        sales_date, 
        product_id,
        NULL,
        sales_amount from offline_sale
) os
where os.sales_date like '2022-03%'
order by sales_date, product_id, user_id;