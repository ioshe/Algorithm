-- 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문
with 
    highest_mem as (
        SELECT 
            MEMBER_ID,
            SUM(REVIEW_SCORE) AS SR
        FROM 
            REST_REVIEW
        GROUP BY
            MEMBER_ID
        ORDER BY
            SR DESC
        LIMIT 1    
)

SELECT
    MEMBER_NAME,
    REVIEW_TEXT,
    DATE_FORMAT(REVIEW_DATE,"%Y-%m-%d") as DATE_FORMAT
FROM 
    REST_REVIEW AS RR
JOIN
    MEMBER_PROFILE AS MP
ON 
    RR.MEMBER_ID = MP.MEMBER_ID
WHERE 
    RR.MEMBER_ID = (SELECT MEMBER_ID FROM highest_mem)
ORDER BY
    DATE_FORMAT,
    REVIEW_TEXT
