from Graph import PyGraph as pygraph
import copy
import random

class LocationFinder (object):

    def __init__(self,initDict={}):

        self.map = pygraph(copy.deepcopy(initDict))
        self.original = pygraph(copy.deepcopy(initDict))    #This property is used to preserve the original graph
        self.result = []
        self.decisions = {}
        
    def warhouseLocation(self):     #A wrappe around findWarehouseLocation()
        self.findWarehouseLocation(self.map)
        
    def findWarehouseLocation(self,graph):      #Find on which verticies should the warehouse be

        temp = []
        for vertex in graph.graphDict.keys():       #Find vertices of degree 0 or 1
            if len(graph.graphDict[vertex]) == 0 and not self.hasNeighbouringWarehouse(vertex,self.original):       #Add warehouse to vertices of degree 0 if it is not a neighbour to the warehouse
                temp.append(vertex)
            if len(graph.graphDict[vertex]) == 1 and not self.hasNeighbouringWarehouse(vertex,self.original):       #Add warehouse to the neighbour of vertex of degree 1 if it is not a neighbour to the warehouse
                temp.append(graph.neighbours(vertex)[0])
        
        for ver in temp:
            self.addWarehouse(ver)

        if self.endFinding():
            print self.result
            return self.result
            
        sortedVertices = graph.sortedKeysWithOutdegree()        #Sort vertices by outdegrees of the vertices
        
        warehouseLocation = [sortedVertices[0]]         #Find the vertex with the greatest weight
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
        self.addWarehouse(warehouseLocation[randomIndex])        #Add warehouse to a random vertex from the list when several are found with same greatest weight
        
        if self.endFinding():
            print self.result
            return self.result
        else:
            self.findWarehouseLocation(graph)       #Proceed recursively

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
