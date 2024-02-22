-- 코드를 입력하세요
SELECT
    INGREDIENT_TYPE,
    SUM(FH.TOTAL_ORDER) as TOTAL_ORDER
FROM 
    FIRST_HALF AS FH
JOIN
    ICECREAM_INFO  AS II
ON FH.FLAVOR = II.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER