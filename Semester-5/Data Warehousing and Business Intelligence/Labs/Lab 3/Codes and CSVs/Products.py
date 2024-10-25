import pyodbc

# Database connection
conn = pyodbc.connect(
"Driver={ODBC Driver 17 for SQL Server};"
"Server=RS\REHAN;"  # Replace with your actual server name
"Database=Northwinds;"               # Replace with your database name
"Trusted_Connection=yes;")

cursor = conn.cursor()



def populate_from_csv(filename,heads,col_count, n):
    places = "("
    for i in range(col_count):
        places+="?"
        if i == col_count-1:
            continue
        else:
            places+=","
    places+=")"
    with open(f"{filename}.csv","r") as file:
        file.readline()
        for i in range(n):
            r = file.readline().split(",")
            r[-1] = r[-1].strip(" \n")
            cursor.execute(f"INSERT INTO {filename} {heads} VALUES {places}", r)

populate_from_csv("Products","(ProductID,ProductName,SupplierID,CategoryID,Unit,Price)", 6, 25)


conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")