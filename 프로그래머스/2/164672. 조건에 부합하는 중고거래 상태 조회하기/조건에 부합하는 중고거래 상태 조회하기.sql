-- 코드를 입력하세요
SELECT BOARD_ID,WRITER_ID,TITLE,PRICE,
CASE 
    WHEN U.STATUS = "SALE" THEN "판매중" 
    WHEN U.STATUS = "RESERVED" THEN "예약중"
    WHEN U.STATUS = "DONE" THEN "거래완료"
END as STATUS
FROM USED_GOODS_BOARD U
WHERE U.CREATED_DATE = '2022-10-05'
ORDER BY BOARD_ID DESC



# 2022년 10월 5일에 등록된