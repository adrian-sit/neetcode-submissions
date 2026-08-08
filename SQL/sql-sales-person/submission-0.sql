-- Write your query below
SELECT name
FROM sales_person
WHERE NOT EXISTS ((
    SELECT 1
    FROM orders
    JOIN company
    ON orders.com_id = company.com_id
    WHERE orders.sales_id = sales_person.sales_id
    AND company.name = 'CRIMSON'
))