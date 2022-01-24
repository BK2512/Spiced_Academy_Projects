--Categories:
drop table cat;
CREATE table cat (categoryID float PRIMARY KEY,categoryName varchar(200),description varchar(200),picture varchar(500));
\copy cat FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\categories.csv' DELIMITER ',' CSV HEADER;

--customers:
drop table cust;
CREATE table cust (customerID varchar(200) PRIMARY KEY,companyName varchar(200),contactName varchar(200),contactTitle varchar(200),
address varchar(200),city varchar(200),region varchar(200),postalCode varchar(200),country varchar(200),
phone varchar(200),fax varchar(200));
\copy cust FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\customers.csv' DELIMITER ',' CSV HEADER;

--Employee_terri:
drop table empti;
CREATE table empti (employeeID float PRIMARY KEY,territoryID float);
\copy empti FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\employee_territories.csv' DELIMITER ',' CSV HEADER;

--employees:
drop table emp;
CREATE table emp (employeeID varchar(200) PRIMARY KEY,lastName varchar(200),firstName varchar(200),title varchar(200),
titleOfCourtesy varchar(200),birthDate varchar(200),hireDate varchar(200),address varchar(200),city varchar(200),
region varchar(200),postalCode varchar(200),country varchar(200),homePhone varchar(200),extension varchar(200),
photo varchar(400),notes varchar(400),reportsTo varchar(400),photoPath varchar(200));
\copy emp FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\employees.csv' DELIMITER ',' CSV HEADER;

--order_details:
drop table orddet;
CREATE table orddet (orderID float PRIMARY KEY,productID float,unitPrice float,quantity float,discount float);
\copy orddet FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\order_details.csv' DELIMITER ',' CSV HEADER;

--orders:
drop table ord;
CREATE table ord (orderID float PRIMARY KEY,customerID varchar(200),employeeID float,orderDate varchar(200),requiredDate varchar (200),
shippedDate varchar(200),shipVia float,freight varchar(200),shipName varchar(200),shipAddress varchar(200),shipCity varchar(200),
shipRegion varchar(200),shipPostalCode varchar(200),shipCountry varchar(200));
\copy ord FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\orders.csv' DELIMITER ',' CSV HEADER;

--products:
drop table prod;
CREATE table prod (productID float PRIMARY KEY,productName text,
supplierID float,categoryID float,quantityPerUnit varchar(200),
unitPrice float,unitsInStock float,unitsOnOrder float,reorderLevel float,discontinued float);
\copy prod FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\products.csv' DELIMITER ',' CSV HEADER;

--regions:
drop table regi;
CREATE table regi (regionID float PRIMARY KEY,regionDescription varchar(200));
\copy regi FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\regions.csv' DELIMITER ',' CSV HEADER;

--shippers:
drop table shipp;
CREATE table shipp (shipperID float PRIMARY KEY,companyName varchar(200),phone varchar(200));
\copy shipp FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\shippers.csv' DELIMITER ',' CSV HEADER;

--suppliers:
drop table supp;
CREATE table supp (supplierID float PRIMARY KEY,companyName varchar(200),contactName varchar(200),
contactTitle varchar(200),address varchar(200),city varchar(200),region varchar(200),
postalCode varchar(200),country varchar(200),phone varchar(200), fax varchar(200),homepage varchar(200));
\copy supp FROM 'C:\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\suppliers.csv' DELIMITER ',' CSV HEADER;

--territories:
drop table terri;
CREATE table terri (territoryID float PRIMARY KEY,
territoryDescription varchar(200),
regionID float);
\copy terri FROM '\Users\bened\Desktop\Northwind\northwind_data_clean-master\data\territories.csv' DELIMITER ',' CSV HEADER;