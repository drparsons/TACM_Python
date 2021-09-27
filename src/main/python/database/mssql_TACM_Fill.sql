USE TACM
GO

BEGIN TRANSACTION

-- Insert rows into table 'UserInfo'
INSERT INTO dbo.UserInfo
( -- columns to insert data into
    [UserInfoID], [UserInfoFirstName], [UserInfoLastName], [UserInfoUsername], [UserInfoPassword], [UserInfoEmail]
)
VALUES
(1, N'David', N'Parsons',
 N'6fYeo6wr9wrM6.bTWX7494tpXRJ6.opg51Wly5hE91o$dwFAjcTnaYu1ia4QvcfIqErtyyiCITeJ7WujtUUeB8Q', 
 N'6fYeo6wr9wrM6.bTWX7494tpXRJ6.opg51Wly5hE91o$dwFAjcTnaYu1ia4QvcfIqErtyyiCITeJ7WujtUUeB8Q', 
 N'drgparsons@gmail.com')
GO

INSERT INTO dbo.Day
(
    [DayID], [DayDate], [DayStartTime], [DayEndTime], [UserInfoId]
)
VALUES
(1, CONVERT(DATE, '2021-09-26', 102), '11:30:00', '12:30:00', 1)


COMMIT;