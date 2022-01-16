import random

class Edge():
    def __init__(self,node1,node2,weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def get_Weight(self):
        return self.weight

    def get_Node_Random(self):
        if random.random() < 0.5:
            return self.node1
        else:
            return self.node2

    def get_Node_Pair(self):
        return (self.node1,self.node2)

    def get_Node_Either(self,node):
        if node == self.node1:
            return self.node2
        elif node == self.node2:
            return self.node1
        else:
            return "节点有误"

class EdgeWeightedGraph():
    def __init__(self,nodeSize):
        self.__nodeSize = nodeSize
        self.__edge = 0
        self.__tableList = [ [] for _ in range(self.__nodeSize)]

    def get_NodeSize(self):
        return self.__nodeSize

    def get_NodeList(self,node):
        return self.__tableList[node]

    def get_TableList(self):
        return self.__tableList

    def get_EdgeSize(self):
        return self.__edge

    def add_Edge(self,node1,node2,weight):
        edge = Edge(node1,node2,weight)
        self.__tableList[node1].append(edge)
        self.__tableList[node2].append(edge)
        self.__edge += 1

    def get_allEdges(self):
        edges = []
        for i in range(self.__nodeSize):
            for e in self.__tableList[i]:
                if e.get_Node_Either(i) < i:
                    edges.append(e)
        return edges

if __name__ == '__main__':
    ewg = EdgeWeightedGraph(5)
    ewg.add_Edge(0, 1, 0.5)
    ewg.add_Edge(2, 3, 0.7)
    ewg.add_Edge(2, 4, 0.9)
    ewg.add_Edge(1, 3, 0.8)

    print(len(ewg.get_allEdges()))
