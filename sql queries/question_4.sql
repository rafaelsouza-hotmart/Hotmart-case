SELECT p.niche,
      SUM(s.cancelled) + SUM(s.refund) AS total_cancellations_refunds
FROM product p
        JOIN sales s ON p.product_id = s.product_id
GROUP BY p.niche
ORDER BY total_cancellations_refunds DESC;