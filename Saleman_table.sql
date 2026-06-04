CREATE TABLE IF NOT EXISTS Salesman (
Salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
Commission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, Commission) VALUES
('S001', 'John Doe', 'New York', 0.10),
('S002', 'Jane Smith', 'Los Angeles', 0.15),
('S003', 'Emily Davis', 'Chicago', 0.12),
('S004', 'Michael Brown', 'Houston', 0.08),
('S005', 'Sarah Wilson', 'Phoenix', 0.20);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders (
ord_no TEXT PRIMARY KEY,
purch_amt REAL,
ord_date TEXT,
customer_id TEXT,
Salesman_id TEXT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, Salesman_id) VALUES
('O001', 500.00, '2024-01-15', 'C001', 'S001'),
('O002', 750.00, '2024-02-20', 'C002', 'S002'),
('O003', 300.00, '2024-03-10', 'C003', 'S003'),
('O004', 450.00, '2024-04-05', 'C004', 'S004'),
('O005', 600.00, '2024-05-25', 'C005', 'S005');

SELECT * FROM Orders;

SELECT name, Commission
FROM Salesman;