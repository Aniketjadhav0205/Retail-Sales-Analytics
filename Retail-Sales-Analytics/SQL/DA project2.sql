create database retail_sales;

USE retail_sales;

create table customer(
customer_id varchar(10)primary key,
Name varchar(100),
email varchar(100),
region varchar(50),
segment varchar(20),
signup_date date
);	

create table products(
product_id varchar(100),
product_name varchar(50),
category varchar(50) ,   
subcategory varchar(50),    
cost_price varchar(50),      
profit varchar(50),          
selling_price varchar(50)
);
create table Stores(
store_id varchar(100),      
store_name varchar(50),   
city  varchar(50),        
state varchar(10),        
region varchar(50),       
store_type varchar(10)
);
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    store_id VARCHAR(10),
    order_date DATE,
    channel VARCHAR(20),
    status VARCHAR(20)
);
CREATE TABLE order_items (
    item_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10),
    product_id VARCHAR(10),
    quantity INT,
    unit_price DECIMAL(10,2),
    discount DECIMAL(5,2)
);

select * from products;
ALTER TABLE products
ADD PRIMARY KEY (product_id);

select * from Stores;
ALTER TABLE Stores
ADD PRIMARY KEY (store_id);

ALTER TABLE orders
MODIFY COLUMN customer_id VARCHAR(10) NOT NULL;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id);

ALTER TABLE orders
MODIFY COLUMN store_id VARCHAR(10) NOT NULL;

ALTER TABLE orders
ADD CONSTRAINT fk_orders_store
FOREIGN KEY (store_id)
REFERENCES stores(store_id);


alter table order_items
add CONSTRAINT fk_order_items_orders
FOREIGN KEY (order_id) 
REFERENCES orders(order_id);

alter table order_items
add CONSTRAINT fk_order_items_products
FOREIGN KEY (product_id) REFERENCES products(product_id);

SHOW CREATE TABLE orders;


RENAME TABLE customer TO customers;

DESCRIBE customers;
DESCRIBE products;
DESCRIBE stores;
DESCRIBE orders;
DESCRIBE order_items;

ALTER TABLE products
MODIFY COLUMN cost_price DECIMAL(10,2);
ALTER TABLE products
MODIFY COLUMN selling_price DECIMAL(10,2);
ALTER TABLE products
MODIFY COLUMN profit DECIMAL(10,2);	
ALTER TABLE stores
MODIFY COLUMN store_type VARCHAR(20);
ALTER TABLE stores
MODIFY COLUMN state VARCHAR(50);

DESCRIBE orders;
SELECT COUNT(*) AS order_id 
FROM orders;
SELECT*FROM orders;

SELECT region FROM customers;
SELECT DISTINCT region
FROM customers;



SELECT *
FROM products
ORDER BY selling_price DESC;

SELECT category,
       COUNT(*) AS total_products
FROM products
GROUP BY category;

SELECT customer_id,
name,
segment
from customers 
where segment in('VIP','New','At-Risk');

select product_id,
product_name,
selling_price
from products
where selling_price between 5000 AND 15000;

SELECT customer_id,
name,
signup_date
from customers 
where signup_date between '2023-01-01' AND '2023-12-31';

SELECT customer_id,
name
from customers 
Where name like 'A%';

select product_id,
product_name,
selling_price
from products
order by selling_price desc
limit 10;

SELECT COUNT(*) AS total_customers
FROM customers;

select count(*)AS Vip_customers
from customers
where segment ='VIP';

select min(selling_price)AS min_selling_price,
max(selling_price)AS max_selling_price
from products;

SELECT
    region,
    COUNT(*) AS total_customers
FROM customers
GROUP BY region
having count(*)>2000;

SELECT
category,
count(*)as total_products,
AVG(selling_price) AS avg_selling_price
FROM products
GROUP BY category
order by selling_price desc;

SELECT
category,
COUNT(*) AS total_products,
AVG(selling_price) AS avg_selling_price
FROM products
GROUP BY category
ORDER BY AVG(selling_price) DESC;

SELECT
    o.order_id,
    c.name,
    s.store_name,
    s.city
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN stores AS s
    ON o.store_id = s.store_id;
    


  
  SELECT
    o.order_id,
    c.name,
    p.product_name,
    oi.quantity
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN order_items AS oi
    ON o.order_id = oi.order_id
INNER JOIN products AS p
    ON oi.product_id = p.product_id;

#order_id
#customer_name
#store_name
#product_name
#quantity
SELECT * FROM retail_sales.customers;
SELECT * FROM retail_sales.orders;
SELECT * FROM retail_sales.stores;
SELECT * FROM retail_sales.products;
SELECT * FROM retail_sales.order_items;


SELECT
    o.order_id,
    c.name, #
    s.store_name,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.discount
FROM orders AS o
INNER JOIN customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN order_items AS oi
    ON o.order_id = oi.order_id
INNER JOIN products AS p
    ON oi.product_id = p.product_id
 INNER JOIN stores AS s
	ON s.store_id = o.store_id;
    
    
#customer_id
#name
#order_id

SELECT
c.customer_id,
c.name,
o.order_id 
FROM customers AS c
Left JOIN Orders AS o
ON o.customer_id = c.customer_id
where order_id is null; 


SELECT 
p.product_name,
oi.order_id
FROM products As p
LEFT JOIN order_items AS oi
ON p.product_id = oi.product_id
where order_id is null;


SHOW DATABASES;



SELECT COUNT(*) AS Orders FROM orders;

SELECT COUNT(*) AS Order_Items FROM order_items;

SELECT COUNT(*) AS Customers FROM customers;

SELECT COUNT(*) AS Products FROM products;

SELECT COUNT(*) AS Stores FROM stores;

SHOW CREATE TABLE order_items;

SHOW CREATE TABLE orders;

Drop table order_items;
Drop table orders;