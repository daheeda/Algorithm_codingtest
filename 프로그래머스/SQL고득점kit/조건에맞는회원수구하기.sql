-- 코드를 입력하세요
SELECT COUNT(U.USER_ID) USERS
FROM USER_INFO U
WHERE DATE_FORMAT(U.JOINED,'%Y') = '2021'
AND U.AGE >= 20
AND U.AGE <= 29
