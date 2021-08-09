"""
Name: David Parsons
Date: 07/09/2021
TACM Task Class
Description: Type of task 
"""

class Type():
#Name
#Description
#Charge Code
#Comments
    def __init__(self, Name=" ", Desc=" ", chg=" ", comment=" "):
        self.name = Name
        self.desc = Desc
        self.chg = chg
        self.comment = comment

    def __str__(self):
        return self.name
##Getters and Setters to be called via createTask()
    def setName(self, Name):
        self.name = Name

    def setDesc(self, Desc):
        self.desc = Desc
    
    def setChg(self, chg):
        self.chg = chg
    
    def setComment(self, comment):
        self.comment = comment

    def getName(self):
        return self.name

    def getDesc(self):
        return self.desc

    def getChg(self):
        return self.chg 
    
    def getComment(self):
        return self.comment
#method with hooks for gui


if __name__ == "__main__":
    print("Hello World!")
    type0 = Type()
    print(type0)
    type0.setName("Set")
    print(type0)
    type1 = Type("TestName", "TestDescription", "CHG001", "TestComment")
    print(type1)
    print("Name: ", type1.getName())
    print("Desc: ", type1.getDesc())
    print("Chg: ", type1.getName())
    print("Comment: ", type1.getComment())