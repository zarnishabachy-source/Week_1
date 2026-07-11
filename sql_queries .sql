-- RetailHub SQL Queries (retailhub.db, tables: sales, payments)

1. Customers from Lahore
SELECT DISTINCT customer_id, customer_name, email, city FROM sales WHERE city = 'Lahore';

2. Ten most expensive products
SELECT DISTINCT product_name, price FROM sales ORDER BY price DESC LIMIT 10;

3. Total revenue
SELECT ROUND(SUM(net_revenue), 2) AS total_revenue FROM sales;

4. Average order value
SELECT ROUND(AVG(net_revenue), 2) AS avg_order_value FROM sales;

5. Total customers
SELECT COUNT(DISTINCT customer_id) AS total_customers FROM sales;

6. Total orders
SELECT COUNT(DISTINCT order_id) AS total_orders FROM sales;

7. Highest spending customers
SELECT customer_id, customer_name, ROUND(SUM(net_revenue),2) AS total_spent FROM sales GROUP BY customer_id, customer_name ORDER BY total_spent DESC LIMIT 10;

8. Pending payments
SELECT p.payment_id, p.order_id, s.customer_name, p.payment_method, p.payment_status FROM payments p LEFT JOIN sales s ON p.order_id = s.order_id WHERE p.payment_status = 'Pending';

9. Monthly revenue
SELECT order_month, ROUND(SUM(net_revenue),2) AS revenue FROM sales GROUP BY order_month ORDER BY order_month;

10. Products sold more than 20 times
SELECT product_name, SUM(quantity) AS units_sold FROM sales GROUP BY product_name HAVING SUM(quantity) > 20 ORDER BY units_sold DESC;

11. Customers by city
SELECT city, COUNT(DISTINCT customer_id) AS num_customers FROM sales GROUP BY city ORDER BY num_customers DESC;

12. Most popular payment method
SELECT payment_method, COUNT(*) AS usage_count FROM payments WHERE payment_method != 'Unknown' GROUP BY payment_method ORDER BY usage_count DESC LIMIT 1;

