class DiEdge():
    def __init__(self,node1,node2,weight):
        self.start = node1
        self.end = node2
        self.weight = weight

    def get_Weight(self):
        return self.weight

    def get_Start_Node(self):
        return self.start

    def get_End_Node(self):
        return self.end

    def get_Node_Pair(self):
        return (self.start,self.end)

    def reverse(self):
        return DiEdge(self.end,self.start,self.weight)

class EdgeWeightedDigraph():
    def __init__(self,nodeSize):
        self.__nodeSize = nodeSize
        self.__edge = 0
        self.__tableList = [ [] for _ in range(self.__nodeSize)]
        self.__reverseList = [[] for _ in range(self.__nodeSize)]

    def get_NodeSize(self):
        return self.__nodeSize

    def get_NodeList(self,node):
        return self.__tableList[node]

    def get_TableList(self):
        return self.__tableList

    def get_EdgeSize(self):
        return self.__edge

    def add_Edge(self,node1,node2,weight):
        edge = DiEdge(node1,node2,weight)
        self.__tableList[node1].append(edge)
        self.__reverseList[node2].append(edge.reverse())
        self.__edge += 1

    def reverse(self):
        rewdg = EdgeWeightedDigraph(self.__nodeSize)
        rewdg.__tableList = self.__reverseList
        rewdg.__reverseList = self.__tableList
        rewdg.__edge = self.__edge
        return rewdg

    def get_allEdges(self):
        edges = []
        for i in range(self.__nodeSize):
            for e in self.__tableList[i]:
                edges.append(e)
        return edges

if __name__ == '__main__':
    ewdg = EdgeWeightedDigraph(5)
    ewdg.add_Edge(0, 1, 0.5)
    ewdg.add_Edge(2, 3, 0.7)
    ewdg.add_Edge(2, 4, 0.9)
    ewdg.add_Edge(1, 3, 0.8)

    print([e.get_Node_Pair() for e in ewdg.get_allEdges()])
    print([e.get_Node_Pair() for e in ewdg.reverse().get_allEdges()])