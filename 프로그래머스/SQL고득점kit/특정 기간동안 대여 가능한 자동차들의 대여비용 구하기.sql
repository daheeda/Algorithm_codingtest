SELECT A.CAR_ID, A.CAR_TYPE, ROUND((1-C.DISCOUNT_RATE/100)*A.DAILY_FEE*30) FEE
FROM CAR_RENTAL_COMPANY_CAR A
    JOIN (SELECT *, CASE
                    WHEN '2022-11' BETWEEN DATE_FORMAT(B.START_DATE, '%Y-%m') 
                        AND DATE_FORMAT(B.END_DATE, '%Y-%m')
                    THEN 1
                    ELSE 0 END AS BB
          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY B
         ) AS B ON B.CAR_ID = A.CAR_ID
    INNER JOIN (SELECT *
        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN C
         WHERE C.DURATION_TYPE = '30일 이상' AND C.CAR_TYPE IN ('세단','SUV')) 
         AS C ON C.CAR_TYPE = A.CAR_TYPE
WHERE (1-C.DISCOUNT_RATE/100)*A.DAILY_FEE*30>=500000 AND (1-C.DISCOUNT_RATE/100)*A.DAILY_FEE*30 <2000000 
GROUP BY A.CAR_ID
HAVING SUM(B.BB)=0
ORDER BY FEE DESC, A.CAR_TYPE , A.CAR_ID DESC

/*


SELECT c.car_id, c.car_type,
       FLOOR(c.daily_fee * 30 * (1 - p.discount_rate/100)) fee
FROM CAR_RENTAL_COMPANY_CAR c
INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
ON c.car_type = p.car_type
   AND p.duration_type = '30일 이상'
   AND c.car_type IN ('SUV', '세단')
LEFT OUTER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
ON c.car_id = h.car_id
   AND h.end_date >= '2022-11-01' AND h.start_date <= '2022-11-30'
WHERE ROUND(c.daily_fee * 30 * (1 - p.discount_rate/100)) BETWEEN 500000 AND 1999999
      AND h.car_id IS NULL
ORDER BY fee DESC, c.car_type, c.car_id DESC;*/
