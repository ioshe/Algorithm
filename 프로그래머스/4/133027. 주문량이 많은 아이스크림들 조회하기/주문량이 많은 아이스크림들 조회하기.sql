with 
    SUM_JU AS (
        SELECT 
            SHIPMENT_ID,
            FLAVOR,
            SUM(TOTAL_ORDER) AS TOTAL_ORDER
        FROM
            JULY
        GROUP BY 
            FLAVOR),
        
    SUM_FH AS (
        SELECT 
            SHIPMENT_ID,
            FLAVOR,
            SUM(TOTAL_ORDER) AS TOTAL_ORDER
        FROM
            FIRST_HALF
        GROUP BY 
            FLAVOR)
            
SELECT FLAVOR
FROM(   
    SELECT 
        SJ.FLAVOR,
        (SJ.TOTAL_ORDER + SF.TOTAL_ORDER) AS TOTAL_ORDER 
    FROM SUM_JU AS SJ
    JOIN SUM_FH AS SF
    ON SJ.FLAVOR = SF.FLAVOR
    GROUP BY 
        FLAVOR
    ORDER BY
        TOTAL_ORDER DESC) as ls
LIMIT 3
    