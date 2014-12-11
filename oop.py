class yolo:
    empcount=0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        yolo.empcount += 1

    def displaycount(self):
        print "total Emp %d" % yolo.empcount

    def displayemp(self):
        print "Name: ", self.name, "sal:", self.salary


emp1 = yolo("chuck", 5)
emp2 = yolo("dill", 6)


emp1.displayemp()
emp2.displayemp()
