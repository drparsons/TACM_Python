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
        #End Time
        self.end = time.time()

    #duration()
    def duration(self):
        #Returns seconds
        duration = (self.end - self.start)
        if duration < 60:
            return "%.2f" % (self.end - self.start)
        else:
            return time.strftime("%I:%M:%S", time.gmtime(duration))

    #getters and setters
    def setStart(self):
        self.start = time.time()

    def setEnd(self):
        self.end = time.time()

    def getStart(self):
        return time.strftime("%I:%M:%S %p", time.localtime(self.start)) #self.startString
    
    def getEnd(self):
        return time.strftime("%I:%M:%S %p", time.localtime(self.end))

    def customSetStart(self, timeString):
        self.start = self.timeInSeconds(timeString)

    def customSetEnd(self, timeString):
        self.end = self.timeInSeconds(timeString)

    #utility functions
    def timeInSeconds(self, timeString):
        #current local time in seconds
        todaySeconds = time.time() - self.convertToSeconds(time.strftime("%I:%M:%S %p", time.localtime()))
        return self.convertToSeconds(timeString) + todaySeconds


    def convertToSeconds(self, timeString):
        #Expecting (HH:MM:SS AM)
        #           01:34:67 9
        hours = float(timeString[0:2])
        minutes = float(timeString[3:5])
        seconds = float(timeString[6:8])
        amORpm = 432000 if timeString[9:11].lower() == "pm" else 0
        totalSeconds = (hours * 3600) + (minutes * 60) + seconds + amORpm
        return totalSeconds


if __name__ == "__main__":
    print("5 second timer:")
    task1 = Event()
    #task1.setStart()
    time.sleep(5)
    task1.setEnd()
    print("Start:",task1.getStart(),"\nEnd  :",task1.getEnd(),"\nDuration:",task1.duration())
    print(task1.convertToSeconds("03:55:05 AM")) #should be 14105.0
    print(task1.convertToSeconds("03:55:05 PM")) #soulld be 446105
    task2 = Event()
    task2.customSetStart("03:55:05 AM")
    task2.customSetEnd("03:55:05 PM")
    print("Start:",task2.getStart(),"\nEnd  :",task2.getEnd(),"\nDuration:",task2.duration())
