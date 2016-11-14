from Graph import PyGraph as pygraph
import copy
import random
import time

g = {'1':['2','6','5'],'2':['1','5','3'],'3':['2','5','8','9','4'],'4':['3','9'],'5':['1','2','3','7','6'],'6':['1','5','10'],'7':['5','7','11','10'],'8':['3','9','12','11','7'],'9':['3','4','12','8'],'10':['6','7','11'],'11':['10','7','8','12'],'12':['11','8','9']}

class LocationFinder (object):

    def __init__(self,initDict={}):

        self.map = pygraph(copy.deepcopy(initDict))
        self.original = pygraph(copy.deepcopy(initDict))    #This property is used to preserve the original garph
        self.result = []
        self.decisions = {}
        
    def warhouseLocation(self):
        self.findWarehouseLocation(self.map)
        
    def findWarehouseLocation(self,graph):      #Find on which verticies should the warehouse be

        temp = []
        for vertex in graph.graphDict.keys():       #Find vertices of degree 0 or 1
            if len(graph.graphDict[vertex]) == 0 and not self.hasNeighbouringWarehouse(vertex,self.original):       #Add warehouse to vertices of degree 0
                temp.append(vertex)
            if len(graph.graphDict[vertex]) == 1 and not self.hasNeighbouringWarehouse(vertex,self.original):       #Add warehouse to the neighbour of vertes of degree 1 if it is not a neighbour to the warehouse
                temp.append(graph.neighbours(vertex)[0])
        
        for ver in temp:
            self.addWarehouse(ver)

        if self.endFinding():
            print self.result
            return self.result
            
        sortedVertices = graph.sortedKeysWithOutdegree()        #Find the vertex with the highest outdegree
        
        warehouseLocation = [sortedVertices[0]]         #Find the vertex with the greates weight
        warehouseWeight = graph.weight(sortedVertices[0])
        for vertex in sortedVertices:
            w = graph.weight(vertex)
            if w == warehouseWeight:
                warehouseLocation.append(vertex)
                warehouseWeight = w
            if w > warehouseWeight:
                warehouseLocation = [vertex]
                warehouseWeight = w

        randomIndex = random.randrange(0,len(warehouseLocation)-1,1)
        self.addWarehouse(warehouseLocation[randomIndex])        #Add warehouse to the vertex
        
        if self.endFinding():
            print self.result
            return self.result
        else:
            self.findWarehouseLocation(graph)

    def addWarehouse(self,vertex):
        self.result.append(vertex)
        self.map.removeWarehouseVertex(vertex)
        
    def endFinding(self):
        for vertex in self.map.vertices():
            if not self.hasNeighbouringWarehouse(vertex,self.original):
                return False
        return True

    def hasNeighbouringWarehouse(self,vertex,original):
        for neighbour in original.neighbours(vertex):
            if neighbour in self.result:
                return True
        return False
    
    def importFromMatrix(self):
        return

l = LocationFinder(g)
l.warhouseLocation()
## http://stackoverflow.com/questions/18761766/mergesort-python
