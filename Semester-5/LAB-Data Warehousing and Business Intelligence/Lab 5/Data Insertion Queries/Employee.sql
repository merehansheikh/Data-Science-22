INSERT INTO Employee (EmployeeKey, FirstName, LastName, Title, BirthDate, HireDate, Address, City, Region, PostalCode, Country, SupervisorKey)
VALUES
    (1, 'John', 'Doe', 'Manager', '1980-01-01', '2023-01-01', '123 Main St', 'Anytown', 'CA', '12345', 'USA', 1),
    (2, 'Jane', 'Smith', 'Salesperson', '1985-02-15', '2023-02-15', '456 Elm St', 'Anytown', 'CA', '54321', 'USA', 1),
    (3, 'Michael', 'Johnson', 'Engineer', '1990-03-20', '2023-03-20', '789 Oak St', 'Anytown', 'CA', '98765', 'USA', 1),
    (4, 'Emily', 'Davis', 'Analyst', '1995-04-05', '2023-04-05', '101 Pine St', 'Anytown', 'CA', '43210', 'USA', 2),
    (5, 'David', 'Wilson', 'Developer', '2000-05-10', '2023-05-10', '202 Cedar St', 'Anytown', 'CA', '87654', 'USA', 2);