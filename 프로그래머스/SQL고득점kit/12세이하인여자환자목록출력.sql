-- 코드를 입력하세요
SELECT P.PT_NAME, P.PT_NO, P.GEND_CD, P.AGE, ifnull(P.TLNO,"NONE") TINO
FROM PATIENT P
WHERE P.GEND_CD = 'W'
AND P.AGE <= 12
ORDER BY P.AGE DESC, P.PT_NAME ASC

/*
IFNULL(expression, alt_value)
# 예시
SELECT IFNULL(NULL, "대체 텍스트");
*/
