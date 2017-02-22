import json

class User:
    def __init__(self, fname, lname, sq, aq):
        self.fname = fname
        self.lname = lname
        self.sq = sq
        self.aq = aq

    def __str__(self):
        return self.fname + " " + self.lname + " " + self.sq + " " + self.aq

    def getfname(self):
        return self.fname

    def getlname(self):
        return self.lname

    def getsq(self):
        return self.sq

    def getaq(self):
        return self.aq








