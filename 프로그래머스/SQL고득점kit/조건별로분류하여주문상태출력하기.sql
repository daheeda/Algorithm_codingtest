SELECT F.ORDER_ID, F.PRODUCT_ID, date_format(F.OUT_DATE,'%Y-%m-%d') OUT_DATE,
        case
        WHEN F.OUT_DATE IS NULL
        THEN '출고미정'
        WHEN F.OUT_DATE <= '2022-05-01'
        THEN '출고완료'
        ELSE '출고대기'
        END AS 출고여부
FROM FOOD_ORDER F
ORDER BY F.ORDER_ID
