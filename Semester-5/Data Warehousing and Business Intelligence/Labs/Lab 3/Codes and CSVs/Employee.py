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

def populate_employee(n):
    for i in range(n):
        data = [i+1,
            fake.last_name(),
            fake.first_name(),
            fake.job(),
            fake.random_element(["Mr.", "Ms.", "Mrs.", "Miss"]),
            fake.date_of_birth(),
            fake.date_between(start_date='-10y', end_date='today'),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.postcode(),
            fake.country(),
            fake.phone_number(),
            fake.random_element([None, fake.random_number(digits=4)]),
            fake.text(),
            fake.image_url()
        ]

        # Insert the data into the table
        cursor.execute("""INSERT INTO Employees 
                       (EmployeeID,LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, Address, City, Region, PostalCode, Country, HomePhone,Extension, Notes, PhotoPath)
                       VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",data)

populate_employee(10)

conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")