class PyNode:       #This is a class implementing a vertex in the graph theory
    def __init__(self,weight=1,name="",tax=0,state=""):
        self.weight = 1
        self.adjNodes = []
        self.name = name
        self.state = state
        self.tax = tax
