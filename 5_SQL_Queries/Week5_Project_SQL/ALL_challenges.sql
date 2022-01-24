-- 1-Get the names and the quantities in stock for each product.
SELECT productID,productName,unitsInStock FROM prod;

-- 2-Get a list of current products (Product ID and name).
SELECT productID,productName FROM prod;

--3-Get a list of the most and least expensive products (name and unit price).
SELECT productName,unitPrice FROM prod WHERE unitPrice=(SELECT MAX(unitPrice)FROM prod);

SELECT productName,unitPrice FROM prod WHERE unitPrice=(SELECT MIN(unitPrice)FROM prod);

-- 4-Get products that cost less than $20.
SELECT productID,productName,unitPrice FROM prod WHERE unitPrice<'20';

-- 5-Get products that cost between $15 and $25.
SELECT productID,productName,unitPrice FROM prod WHERE unitPrice>'15' AND unitPrice<'25';

-- 6-Get products above average price
SELECT productID,productName,AVG(unitPrice) AS avg_price FROM prod GROUP BY productID;

SELECT productName,AVG(unitPrice) FROM prod; --Group by?

-- 7-Find the ten most expensive products.
SELECT productName,unitprice FROM prod ORDER BY unitprice DESC LIMIT 10;

-- 8-Get a list of discontinued products (Product ID and name).
SELECT productname,discontinued FROM prod WHERE discontinued='1';

-- 9-Count current and discontinued products
SELECT COUNT(discontinued) AS counti FROM prod WHERE discontinued=1;
SELECT COUNT(discontinued) AS counti FROM prod WHERE discontinued=0;

-- 10-Find products with less units in stock than the quantity on order.
SELECT productname,unitsInStock,unitsOnOrder FROM prod WHERE unitsInStock<unitsOnOrder;

-- 11-Find the customer who had the highest order amount
SELECT customerID,SUM(freight) AS SUMFreight FROM ord GROUP BY customerID
ORDER BY SUMFREIGHT desc LIMIT 5;