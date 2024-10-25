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

def populate_regions(n):
    for _ in range(n):
        region_id = random.randint(1, 1000)  # Generate random region_id
        region_desc = fake.city_suffix()     # Fake city suffix for region description
        cursor.execute(
            "INSERT INTO Regions (RegionID, RegionDescription) VALUES (?, ?)",
            region_id, region_desc
        )

populate_regions(10)

conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")