-- 코드를 입력하세요
SELECT ROUND(AVG(C.DAILY_FEE),0) AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR AS C
WHERE C.CAR_TYPE = 'SUV'

/*
ROUND(X) ; 
TRUNCATE(X,X) ; CUT
ROUND(X,X)
*/
