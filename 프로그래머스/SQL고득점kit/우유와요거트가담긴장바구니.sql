# SELECT DISTINCT A.CART_ID
# FROM CART_PRODUCTS A 
# INNER JOIN CART_PRODUCTS B ON A.CART_ID = B.CART_ID
# WHERE A.NAME LIKE 'Yogurt' AND B.NAME LIKE 'Milk'
# ORDER BY A.CART_ID

-- 코드를 입력하세요
WITH MILK AS (
    
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = 'Milk'
    GROUP BY CART_ID
)

SELECT C.CART_ID
FROM CART_PRODUCTS C JOIN MILK M ON C.CART_ID = M.CART_ID
WHERE C.NAME = 'Yogurt'
ORDER BY C.CART_ID

# select cart_id
# from (
#     select distinct cart_id
#         , NAME
#     from CART_PRODUCTS
#     where name in ('Milk','Yogurt')) tbl
# group by 1
# having count(cart_id) >= 2
# order by 1
