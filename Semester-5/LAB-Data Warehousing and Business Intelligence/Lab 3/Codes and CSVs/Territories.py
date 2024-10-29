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

def populate_territories(n):
    cursor.execute("SELECT RegionID FROM Regions")  # Get available RegionIDs
    region_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        territory_id = fake.unique.zipcode()          # Fake and unique territory id
        territory_desc = fake.city()                 # Fake city name for description
        region_id = random.choice(region_ids)        # Randomly pick a RegionID
        cursor.execute(
            "INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID) VALUES (?, ?, ?)",
            territory_id, territory_desc, region_id
        )

populate_territories(10)

conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")