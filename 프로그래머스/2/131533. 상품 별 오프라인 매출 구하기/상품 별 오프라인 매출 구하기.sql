-- 코드를 입력하세요
SELECT PRODUCT_CODE, SUM(SALES_AMOUNT) * PRICE AS SALES
FROM PRODUCT
NATURAL JOIN OFFLINE_SALE
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE ASC