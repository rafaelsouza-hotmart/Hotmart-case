-- The top 10 products that sold the most in each niche with deactivated
-- membership area and activated recovery.

SELECT p.product_id, niche, COUNT(p.product_id) AS sales
FROM product p
         JOIN sales s ON p.product_id = s.product_id
WHERE p.recovery_active = 1 AND p.member_area_active = 0
GROUP BY p.product_id, niche
ORDER BY sales DESC
LIMIT 10;