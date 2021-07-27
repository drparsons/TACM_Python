"""
Name: David Parsons
Date: 07/09/2021
TACM Task Class
Description: Type of task 
"""

class Type(self):
#Name
#Description
#Charge Code
#Comments
    def __init__(self, Name=" ", Desc=" ", chg=" ", comment=" "):
        self.name = Name
        self.desc = Desc
        self.chg = chg
        self.comment = comment

##Getters and Setters to be called via createTask()
    def setName(self, Name):
        self.name = Name

    def setDesc(self, Desc):
        self.desc = Desc
    
    def setChg(self, chg):
        self.chg = chg
    
    def setComment(self, comment):
        self.comment = comment

    def getName(self, Name):
        return self.name

    def getDesc(self, Desc):
        return self.desc

    def getChg(self, chg):
        return self.chg 
    
    def getComment(self, comment):
        return self.comment
#method with hooks for gui
