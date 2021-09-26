USE TEST
-- Create a new table called 'testTable' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('dbo.testTable', 'U') IS NOT NULL
DROP TABLE dbo.testTable
GO
-- Create the table in the specified schema
CREATE TABLE dbo.testTable
(
    testTableId INT NOT NULL PRIMARY KEY, -- primary key column
    Name [NVARCHAR](50) NOT NULL,
    Location [NVARCHAR](50) NOT NULL
    -- specify more columns here
);
GO
-- Insert rows into table 'dbo.testTable'
INSERT INTO dbo.testTable
( -- columns to insert data into
 [testTableId], [Name], [Location]
)
VALUES
   ( 1, N'Jared', N'Australia'),
   ( 2, N'Nikita', N'India'),
   ( 3, N'Tom', N'Germany'),
   ( 4, N'Jake', N'United States'),
   ( 5, N'Tommy', N'United States')
GO

-- Select rows from a Table or View 'testTable' in sCOUNT(c) as EmployeeCounthema 'dbo'

SELECT COUNT(*) as EmployeeCount FROM dbo.testTable

-- Select rows from a Table or View 'testTable' in schema 'dbo'

SELECT e.testTableId, e.Name, e.[Location]
FROM dbo.testTable as e	/* add search conditions here */
GO