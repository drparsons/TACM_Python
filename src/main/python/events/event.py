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
        return "%.2f" % (self.end - self.start)

    #getters and setters
    def setStart(self):
        self.start = time.time()

    def setEnd(self):
        self.end = time.time()



if __name__ == "__main__":
    print("5 second timer:")
    task1 = Event()
    #task1.setStart()
    time.sleep(5)
    task1.setEnd()
    print(task1.duration())