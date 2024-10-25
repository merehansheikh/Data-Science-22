import time
import matplotlib.pyplot as plt
import pyodbc

# Database connection
conn = pyodbc.connect(
"Driver={ODBC Driver 17 for SQL Server};"
"Server=RS\REHAN;"  # Replace with your actual server name
"Database=Northwinds;"               # Replace with your database name
"Trusted_Connection=yes;")

cursor = conn.cursor()

queries={
    "Retrieve Order by OrderID": "SELECT * FROM Orders WHERE OrderID = 10258",
    "Retrieve Customer by CustomerID": "SELECT * FROM Customers WHERE CustomerID = '9'",
    "Retrieve Supplier by SupplierID": "SELECT * FROM Suppliers WHERE SupplierID = 15",
    "Retrieve Product by ProductID": "SELECT * FROM Products WHERE ProductID = 7",
    "Retrieve Employee by EmployeeID": "SELECT * FROM Employees WHERE EmployeeID = 34",

    "Retrieve Customer by CustomerName": "SELECT * FROM Customers WHERE CustomerName = 'Old World Bakery'",
    "Retrieve Shipper by CompanyName": "SELECT * FROM Shippers WHERE CompanyName = 'ABC Shipping'",
    "Retrieve Orders by OrderDate": "SELECT * FROM Orders WHERE OrderDate = CONVERT(DATETIME, '2024-10-13', 120)",
    "Retrieve Orders by CustomerName": "SELECT * FROM Orders o JOIN Customers c ON o.CustomerID = c.CustomerID WHERE c.CustomerName = 'Old World Bakery'",
    "Retrieve Orders by Shipper CompanyName": "SELECT * FROM Orders o JOIN Shippers s ON o.ShipperID = s.ShipperID WHERE s.CompanyName = 'ABC Shipping'"
}

execution_times={}
for query_name, query in queries.items():
    start_time=time.time()
    cursor.execute(query)
    cursor.fetchall()
    end_time=time.time()
    execution_times[query_name]=(end_time-start_time)*100

conn.commit()
conn.close()

plt.bar(execution_times.keys(), execution_times.values())
plt.xticks(rotation=45, ha='right')
plt.xlabel('Queries')
plt.ylabel('Execution Time')
plt.title('Query Execution Times')
plt.tight_layout()
plt.show()