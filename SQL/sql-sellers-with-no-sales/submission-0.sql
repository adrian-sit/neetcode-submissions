-- Write your query below
SELECT seller_name
FROM seller
WHERE NOT EXISTS (
    SELECT 1
    FROM orders
    WHERE orders.seller_id = seller.seller_id
    AND orders.sale_date >= '2020-01-01'
    AND orders.sale_date < '2021-01-01'
)
ORDER BY seller_name