CREATE DATABASE Umuzi;

CREATE TABLE Customers (
    CustomerID serial PRIMARY KEY,
    FirstName varchar(50),
    LastName varchar(50),
    Gender varchar,
    Address varchar(200),
    Phone int,
    Email varchar(100),
    City varchar(20),
    Country varchar(50)
);
CREATE TABLE Employees (
    EmployeeID serial PRIMARY KEY,
    FirstName varchar(50),
    LastName varchar(50),
    Email varchar(100),
    JobTitle varchar(20) 
);
CREATE TABLE Payments (
    CustomerID INT,
    PaymentID serial,
    PaymentDate date,
    Amount numeric(10,2),
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) 
);
CREATE TABLE Products (
    ProductID INT,
    ProductName varchar(100),
    Description varchar(300),
    BuyPrice numeric(10,2),
    PRIMARY KEY (ProductID)
);
CREATE TABLE Orders (
    OrderID serial,
    ProductID int,
    PaymentID int,
    FulfilledByEmployeeID int,
    DateRequired date,
    DateShipped date,
    Status varchar(20),
    PRIMARY KEY (OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (PaymentID) REFERENCES Payments(PaymentID),
    FOREIGN KEY (FulfilledByEmployeeID) REFERENCES Employees(EmployeeID)
);

INSERT INTO Customers VALUES(1,'John', 'Hibert', 'Male', '284 chaucer st', 084789657, 'john@gmail.com', 'Johannesburg', 'South Africa');
INSERT INTO Customers VALUES(2, 'Thando', 'Sithole','Female', '240 Sect 1',0794445584, 'thando@gmail.com',	'Cape Town', 'South Africa');
INSERT INTO Customers VALUES(3, 'Leon', 'Glen', 'Male', '81 Everton Rd,Gillits', 0820832830, 'Leon@gmail.com', 'Durban', 'South Africa');
INSERT INTO Customers VALUES(4, 'Charl', 'Muller', 'Male', '290A Dorset Ecke', 0856872553, 'Charl.muller@yahoo.com', 'Berlin', 'Germany');
INSERT INTO Customers VALUES(5, 'Julia', 'Stein', 'Female', '2 Wernerring', 0672445058, 'Js234@yahoo.com', 'Frankfurt', 'Germany');
INSERT INTO Employees VALUES(1, 'Kani',	'Matthew', 'mat@gmail.com', 'Manager');
INSERT INTO Employees VALUES(2, 'Lesly', 'Cronje', 'LesC@gmail.com', 'Clerk');
INSERT INTO Employees VALUES(3,	'Gideon', 'Maduku', 'm@gmail.com', 'Accountant');
INSERT INTO Products VALUES(1, 'Harley Davidson Chopper', 'This replica features working kickstand, front suspension, gear-shift lever', 150.75);
INSERT INTO Products VALUES(2, 'Classic Car', 'Turnable front wheels, steering function', 550.75);
INSERT INTO Products VALUES(3, 'Sports car', 'Turnable front wheels, steering function', 700.60);
INSERT INTO Payments VALUES(1, 1, '2018-09-01', 150.75);
INSERT INTO Payments VALUES(5, 2, '2018-09-03', 150.75);
INSERT INTO Payments VALUES(4, 3, '2018-09-03', 700.60);
INSERT INTO Orders VALUES(1, 1, 1, 2, '05-09-2018', null, 'Not shipped');
INSERT INTO Orders VALUES(2, 1, 2, 2, '04-09-2018', '03-09-2018', 'Shipped');
INSERT INTO Orders VALUES(3, 3, 3, 3, '06-09-2018', null, 'Not shipped');

