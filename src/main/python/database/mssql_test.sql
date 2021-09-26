-- Create a new table called 'Employees' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('dbo.Employees', 'U') IS NOT NULL
DROP TABLE dbo.Employees
GO
-- Create the table in the specified schema
CREATE TABLE dbo.Employees
(
    EmployeesId INT NOT NULL PRIMARY KEY, -- primary key column
    Name [NVARCHAR](50) NOT NULL,
    Location [NVARCHAR](50) NOT NULL
    -- specify more columns here
);
GO

-- Insert rows into table 'dbo.Employees'
INSERT INTO dbo.Employees
( -- columns to insert data into
 [EmployeesId], [Name], [Location]
)
VALUES
   ( 1, N'Jared', N'Australia'),
   ( 2, N'Nikita', N'India'),
   ( 3, N'Tom', N'Germany'),
   ( 4, N'Jake', N'United States')
GO
-- Select rows from a Table or View 'Employees' in sCOUNT(c) as EmployeeCounthema 'dbo'
SELECT COUNT(*) as EmployeeCount FROM dbo.Employees

-- Select rows from a Table or View 'Employees' in schema 'dbo'
SELECT e.EmployeesId, e.Name, e.[Location]
FROM dbo.Employees as e	/* add search conditions here */
GO