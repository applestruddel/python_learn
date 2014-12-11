class person:
    def __init__(self, name):
        self.name = name
    def printname(self):
            print self.name
p = person('tristan burda')
print p.name
p.printname()
