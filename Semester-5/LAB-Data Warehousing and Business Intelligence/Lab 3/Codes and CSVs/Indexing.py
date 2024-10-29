import pyodbc

# Database connection
conn = pyodbc.connect(
"Driver={ODBC Driver 17 for SQL Server};"
"Server=RS\REHAN;"  
"Database=Northwinds;"               
"Trusted_Connection=yes;")

cursor = conn.cursor()

cursor.execute("""CREATE INDEX idx_orderid 
ON Orders(OrderID); """)

cursor.execute("""CREATE INDEX idx_customerid
ON Customers(CustomerID); """)

cursor.execute("""CREATE INDEX idx_supplierid 
ON Suppliers(SupplierID); """)

cursor.execute("""CREATE INDEX idx_productid
ON Products(ProductID); """)

cursor.execute("""CREATE INDEX idx_employeeid 
ON Employees(EmployeeID); """)

cursor.execute("""CREATE INDEX idx_customername
ON Customers(CustomerName); """)

cursor.execute("""CREATE INDEX idx_companyname 
ON Shippers(CompanyName); """)

cursor.execute("""CREATE INDEX idx_orderdate
ON Orders(OrderDate); """)

conn.commit()
conn.close()
print("Indexes created successfully!")