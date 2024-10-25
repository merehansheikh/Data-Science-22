import pyodbc

# Database connection
conn = pyodbc.connect(
"Driver={ODBC Driver 17 for SQL Server};"
"Server=RS\REHAN;"  # Replace with your actual server name
"Database=Northwinds;"               # Replace with your database name
"Trusted_Connection=yes;")

cursor = conn.cursor()

def shippers(filename):
    cursor.execute(f'''CREATE TABLE {filename}
    (ShipperID INT PRIMARY KEY,
    CompanyName VARCHAR(255),
    Phone VARCHAR(24));''')
    
def categories(filename):
    cursor.execute(f'''CREATE TABLE {filename}
                    (CategoryID INT PRIMARY KEY,
                    CategoryName VARCHAR(255),
                    Description TEXT);''')

def customers(filename):
    cursor.execute(f'''CREATE TABLE {filename}
                   (CustomerID VARCHAR(50) PRIMARY KEY,
                    CustomerName VARCHAR(255),
                    ContactName VARCHAR(30),
                    Address VARCHAR(255),
                    City VARCHAR(50),
                    PostalCode VARCHAR(20),
                    Country VARCHAR(50));''')
                   
def suppliers(filename):
    cursor.execute(f"""
    CREATE TABLE {filename} (
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(255),
    ContactName VARCHAR(30),
    Address VARCHAR(255),
    City VARCHAR(50),
    PostalCode VARCHAR(20),
    Country VARCHAR(50),
    Phone VARCHAR(24)
    );""")

def products(filename):
    cursor.execute(f"""
    CREATE TABLE {filename} (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    SupplierID INT,
    CategoryID INT,
    Unit VARCHAR(255),
    Price DECIMAL(10, 2),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    );""")

def orders(filename):
    cursor.execute(f"""
    CREATE TABLE {filename} (
    OrderID INT PRIMARY KEY,
    CustomerID VARCHAR(50),
    EmployeeID INT,
    OrderDate DATE,
    ShipperID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ShipperID) REFERENCES Shippers(ShipperID)
    );""")

def order_details(filename):
    cursor.execute(f"""CREATE TABLE {filename} (
    OrderDetailID INT,
    OrderID INT,
    ProductID INT,
    Quantity SMALLINT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
    );""")

def employee():
    cursor.execute("""
    CREATE TABLE Employees (
        EmployeeID INT PRIMARY KEY,
        LastName VARCHAR(255),
        FirstName VARCHAR(255),
        Title VARCHAR(50),
        TitleOfCourtesy VARCHAR(25),
        BirthDate DATE,
        HireDate DATE,
        Address VARCHAR(255),
        City VARCHAR(50),
        Region VARCHAR(50),
        PostalCode VARCHAR(20),
        Country VARCHAR(50),
        HomePhone VARCHAR(24),
        Extension VARCHAR(4),
        Photo IMAGE,
        Notes TEXT,
        ReportsTo INT,
        PhotoPath VARCHAR(255),
        FOREIGN KEY (ReportsTo) REFERENCES Employees(EmployeeID)
    );""")

def regions():
    cursor.execute("""
    CREATE TABLE Regions (
        RegionID INT PRIMARY KEY,
        RegionDescription VARCHAR(50)
    );""")

def territories():
    cursor.execute("""
        CREATE TABLE Territories (
            TerritoryID VARCHAR(20) PRIMARY KEY,
            TerritoryDescription VARCHAR(50),
            RegionID INT,
            FOREIGN KEY (RegionID) REFERENCES Regions(RegionID)
        );""")

def emp_territories():
    cursor.execute(f"""
    CREATE TABLE EmployeeTerritories (
        EmployeeID INT,
        TerritoryID VARCHAR(20),
        PRIMARY KEY (EmployeeID, TerritoryID),
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
        FOREIGN KEY (TerritoryID) REFERENCES Territories(TerritoryID)
    );""")


def create_tables():
    shippers("Shippers")
    categories("Categories")
    customers("Customers")
    suppliers("Suppliers")
    products("Products")
    orders("Orders")
    order_details("Order_details")
    employee()
    regions()
    territories()
    emp_territories()
    conn.commit()
    print("all tables created!")



def main():

    # create_tables()


    conn.commit()

    # Close the connection
    conn.close()
main()
