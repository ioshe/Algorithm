-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, CONCAT(YEAR(DATETIME),"-",LPAD(MONTH(DATETIME),2,'0'),"-",LPAD(DAY(DATETIME),2,'0')) as 날짜
FROM ANIMAL_INS 
order by ANIMAL_ID