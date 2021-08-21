"""
Name: David Parsons
Date: 07/09/2021
TACM Task Class
Description: Parent of Day and Task. Handle timing.
"""
import time
class Event:
    import time
    def __init__(self):
        #start time
        self.start = time.time()
        self.startString = time.strftime("%H:%M:%S %p")
        #End Time
        self.end = time.time()
        self.endString = time.strftime("%H:%M:%S %p")

    #duration()
    def duration(self):
        #Returns seconds
        return "%.2f" % (self.end - self.start)

    #getters and setters
    def setStart(self):
        self.start = time.time()
        self.startString = time.strftime("%H:%M:%S %p")

    def setEnd(self):
        self.end = time.time()
        self.endString = time.strftime("%H:%M:%S %p")

    def getStart(self):
        return self.startString
    
    def getEnd(self):
        return self.endString


if __name__ == "__main__":
    print("5 second timer:")
    task1 = Event()
    #task1.setStart()
    time.sleep(5)
    task1.setEnd()
    print("Start:",task1.getStart(),"\nEnd  :",task1.getEnd(),"\nDuration:",task1.duration(),"s")