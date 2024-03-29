-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/',F.BOARD_ID,'/',F.FILE_ID,F.FILE_NAME,F.FILE_EXT) FILE_PATH
FROM USED_GOODS_FILE F INNER JOIN (
            SELECT BOARD_ID, VIEWS
            FROM USED_GOODS_BOARD
            GROUP BY BOARD_ID, VIEWS
            ORDER BY VIEWS DESC
            LIMIT 1
            ) B ON F.BOARD_ID = B.BOARD_ID
ORDER BY F.FILE_ID DESC
