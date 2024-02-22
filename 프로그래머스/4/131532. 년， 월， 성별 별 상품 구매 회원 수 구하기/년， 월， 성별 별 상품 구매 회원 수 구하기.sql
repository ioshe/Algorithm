-- 코드를 입력하세요
SELECT
    YEAR(sales_date) AS YEAR,
    MONTH(sales_date) AS MONTH,
    GENDER,
    COUNT(DISTINcT(OS.USER_ID)) AS USERS
FROM
    ONLINE_SALE AS OS
JOIN
    (SELECT 
        USER_ID,
        GENDER
     FROM
        USER_INFO
     WHERE 
        GENDER IS NOT NULL
    ) AS UI
ON OS.USER_ID = UI.USER_ID
GROUP BY 
    YEAR,
    MONTH,
    GENDER
ORDER BY
    YEAR,
    MONTH,
    GENDER