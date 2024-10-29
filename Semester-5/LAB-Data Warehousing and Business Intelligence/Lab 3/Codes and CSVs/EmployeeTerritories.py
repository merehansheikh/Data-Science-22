import pyodbc
from faker import Faker
import random

fake = Faker()

# Database connection
conn = pyodbc.connect(
"Driver={ODBC Driver 17 for SQL Server};"
"Server=RS\REHAN;"  # Replace with your actual server name
"Database=Northwinds;"               # Replace with your database name
"Trusted_Connection=yes;")

cursor = conn.cursor()

def populate_emp_territories(n):
    cursor.execute("SELECT TerritoryID FROM Territories")  # Get available TerritoryIDs
    territory_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT EmployeeID FROM Employees")  # Get available EmpIDs
    emp_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        territory_id = random.choice(territory_ids)        # Randomly pick a TerritoryID
        emp_id = random.choice(emp_ids)        # Randomly pick a EmpID
        cursor.execute(
            "INSERT INTO EmployeeTerritories (TerritoryID, EmployeeID) VALUES (?, ?)",
            territory_id,emp_id
        )

populate_emp_territories(10)

conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")