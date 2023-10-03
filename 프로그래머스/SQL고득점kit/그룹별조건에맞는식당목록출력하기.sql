WITH T AS (

SELECT R.MEMBER_ID,M.MEMBER_NAME, COUNT(*) CNT
FROM REST_REVIEW R JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
GROUP BY R.MEMBER_ID
ORDER BY CNT DESC
LIMIT 1
    
    )
    
SELECT T.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
FROM REST_REVIEW R JOIN T ON R.MEMBER_ID = T.MEMBER_ID
ORDER BY REVIEW_DATE, R.REVIEW_TEXT


/*
다른풀이

SELECT p.member_name 멤버명, r.review_text 리뷰, DATE_FORMAT(r.review_date, '%Y-%m-%d') 리뷰작성일
FROM member_profile p, rest_review r
WHERE p.member_id = r.member_id
      AND p.member_id = (SELECT r.member_id
                        FROM rest_review r
                        GROUP BY r.member_id
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)
ORDER BY 리뷰작성일, 리뷰;


WITH T AS (
    SELECT MEMBER_ID, RANK() OVER (ORDER BY COUNT(*) DESC) RANKING
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
)
SELECT REST_REVIEW.MEMBER_ID
FROM REST_REVIEW JOIN T ON REST_REVIEW.MEMBER_ID = T.MEMBER_ID
WHERE T.RANKING = 1


*/
