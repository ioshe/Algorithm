-- 코드를 입력하세요
WITH TRHEE_WRITE_UPPER AS (
    SELECT WRITER_ID, COUNT(WRITER_ID) as WRITER_ID_COUNT
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(WRITER_ID) >= 3
)
SELECT UU.USER_ID, UU.NICKNAME, CONCAT(UU.CITY,' ',UU.STREET_ADDRESS1,' ',UU.STREET_ADDRESS2) AS 전체주소, CONCAT(              SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8, 4)) AS 전화번호
FROM USED_GOODS_USER UU
RIGHT JOIN TRHEE_WRITE_UPPER TU
ON UU.USER_ID = TU.WRITER_ID
ORDER BY USER_ID DESC