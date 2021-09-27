


USE TACM
GO
/*
-- Create a new database called 'TACM'
-- Connect to the 'master' database to run this snippet
USE master
GO
-- Create the new database if it does not exist already
IF NOT EXISTS (
    SELECT name
        FROM sys.databases
        WHERE name = N'TACM'
)
CREATE DATABASE TACM
GO
*/

BEGIN TRANSACTION

-- Drop the table if it already exists
IF OBJECT_ID('dbo.Task', 'U') IS NOT NULL
DROP TABLE dbo.Task
GO
IF OBJECT_ID('dbo.Day', 'U') IS NOT NULL
DROP TABLE dbo.Day
GO
IF OBJECT_ID('dbo.UserType', 'U') IS NOT NULL
DROP TABLE dbo.UserType
GO
IF OBJECT_ID('dbo.UserInfo', 'U') IS NOT NULL
DROP TABLE dbo.UserInfo
GO

-- Create a new table called 'UserInfo' in schema 'dbo'
CREATE TABLE dbo.UserInfo
(
    UserInfoId INT NOT NULL PRIMARY KEY, -- primary key column
    UserInfoFirstName [NVARCHAR](50) NOT NULL,
    UserInfoLastName [NVARCHAR](50) NOT NULL,
    UserInfoUsername [NVARCHAR](100) NOT NULL,
    UserInfoPassword [NVARCHAR](100) NOT NULL,
    UserInfoEmail [NVARCHAR](200) NOT NULL
);
GO

-- Create a new table called 'Day' in schema 'dbo'
CREATE TABLE dbo.Day
(
    DayId INT NOT NULL PRIMARY KEY, -- primary key column
    DayDate DATE NOT NULL,
    DayStartTime TIME,
    DayEndTime Time,
    -- Foreign Key
    UserInfoId INT NOT NULL,
    FOREIGN KEY (UserInfoId) REFERENCES UserInfo(UserInfoId)
);
GO

-- Create a new table called 'UserType' in schema 'dbo'
CREATE TABLE dbo.UserType
(
    UserTypeId INT NOT NULL PRIMARY KEY, -- primary key column
    TYpeDesc [NVARCHAR](50) NOT NULL,
    TypeChg [NVARCHAR](50) NOT NULL,
    TypeComment [NVARCHAR](256),
    -- Foreign Key
    UserInfoID INT NOT NULL,
    FOREIGN KEY (UserInfoId) REFERENCES UserInfo(UserInfoId)
);
GO

-- Create a new table called 'Task' in schema 'dbo'
CREATE TABLE dbo.Task
(
    TaskId INT NOT NULL PRIMARY KEY, -- primary key column
    TaskName [NVARCHAR] (100) NOT NULL,
    TaskStartTime TIME,
    TaskEndTime TIME,
    -- Foreign Keys
    UserTypeID INT,
    DayID INT NOT NULL,
    FOREIGN KEY (DayID) REFERENCES Day(DayID)
);
GO

COMMIT;