from Node import PyNode as node

class PyGraph (object):     #This is an adjacency-list class that implements the graph theory
    
    def __init__(self,graphDict=None):
        if graphDict == None:
            graphDict = {}
        self.graphDict = graphDict.copy()

    def numberOfVertices(self):
        return len(self.graphDict)

    def vertices(self):
        return self.graphDict.keys()
    
    def edges(self):
        edges = []
        for vertex in self.graphDict:
            for neighbour in self.graphDict[vertex]:
                if (neighbour, vertex) or (vertex,neightbour) not in edges:
                    edges.append((vertex, neighbour))
        return edges
        
    def addDirectedEdge(self,v1,v2):        #Add a directed edge from v1 to v2
        if v1 in self.graphDict and v2 not in self.graphDict[v1]:
            self.graphDict[v1].append(v2)
            return
        print "Error: Vertex not exist or repeated"

    def addVertex(self,vertex,weight=1):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []
            return
        print "Error: Vertex already exist"

##    def verticesOfHighestOutDegree(self):       #Returns the vertices of the highest degree
##        result = []
##        highestOutDegree = len(self.graphDict.values()[0])
##        for vertex in self.graphDict.keys():
##            if self.outDegree(vertex) == highestOutDegree:
##                result.append(vertex)
##            if self.outDegree(vertex) > highestOutDegree:
##                result = [vertex]
##                highestOutDegree = self.outDegree(vertex)
##        return result

    def neighbours(self,vertex):
        if vertex not in self.graphDict:
            print "Error: Vertex does not exit when finding neighbours"
            return
        return self.graphDict[vertex]

    def outDegree(self,vertex):         #The outdegree of a vertex
        if vertex not in self.graphDict:
            print "Error: Vertex does not exit when finding outdegree"
            return None
        return len(self.graphDict[vertex])

    def neighbourOutDegree(self,vertex):        #Returns the list of degrees of the neighbouring vertices
        if vertex not in self.graphDict:
            print "Error: Vertex does not exit when finding neighbourOutDegree"
            return
        neighbourDegree = []
        for neighbour in self.neighbours(vertex):
            neighbourDegree.append(len(self.graphDict[neighbour]))
        return neighbourDegree

    def averageNeighbourOutDegree(self,vertex):
        neighbourOuts = self.neighbourOutDegree(vertex)
        if len(neighbourOuts) == 0:
            return 0
        degreeSum = 0
        for outdegree in neighbourOuts:
            degreeSum += outdegree
        return float(degreeSum)/len(neighbourOuts)
    
    def removeAllOutEdge(self,vertex):
        if vertex in self.graphDict:
            self.graphDict[vertex] = []
            return
        print "Error: Vertex does not exit when removing all inedges"

    def removeAllInEdge(self,vertex):
        if vertex not in self.graphDict:
            print "Error: Vertex does not exit when removing all outedges"
            return
        for vertices in self.graphDict.values():
            if vertex in vertices:
                vertices.remove(vertex)

    def removeWarehouseVertex(self,vertex):         #Removes the vertex where the warehouse is and the edges connected to it, as well as the directed edges pointing to its neighbours, since the warehouse's neighbours do not need goods shipping to them. 
        if vertex not in self.graphDict:
            print "Error: Vertex does not exit when removing warehouse vertex"
            return
        neighbours = self.neighbours(vertex)[:]
        for i in range(0,len(neighbours)):
            self.removeAllInEdge(neighbours[i])
        self.removeAllInEdge(vertex)
        del self.graphDict[vertex]

    def sortedKeysWithOutdegree(self):          #Sorts the vertices by its degrees. Implemented by a merge sort
        x = self.graphDict.keys()
        return self.msort2(x)

    def independentNodeGenerated(self,vertex):          #A variable taken to consider. It indicates how many independent nodes (nodes of degree 0) will be generated when warehouse is located in a specific vertex.
        result = 0
        for neighbour in self.neighbours(vertex):
            if self.outDegree(neighbour) == 1:
                result += 1
        return result

    def averageTax(self,vertex):
        if not isinstance(vertex,node):
            return 0
        result = 0
        for neighbour in self.neighbours(vertex):
            if isinstance(neighbour,node) and neighbour.state != vertex.state:
                result += neighbour.tax
        return float(result)/len(self.neighbours(vertex))
    
    def msort2(self,x):
        if len(x) < 2:
            return x
        result = []
        mid = int(len(x)/2)
        y = self.msort2(x[:mid])
        z = self.msort2(x[mid:])
        while (len(y) > 0) and (len(z) > 0):
                if len(self.graphDict[y[0]]) < len(self.graphDict[z[0]]):
                    result.append(z[0])
                    z.pop(0)
                else:
                    result.append(y[0])
                    y.pop(0)
        result += y
        result += z
        return result

    def weight(self,vertex):        # Offers the weight coefficient of a specific vertex in chosing the location of the warehouse. The weight coefficient is composed of the outdegree of the vertex, the average degree of its neighbouring vertices, and the number of independent vertices generated by the warehouse located at this vertex.
        w = 1 * self.outDegree(vertex) + (-0.1) * self.averageNeighbourOutDegree(vertex) + (-0.4) * self.independentNodeGenerated(vertex) + (-0.1) * self.averageTax(vertex)
        return
