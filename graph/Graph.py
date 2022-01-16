class Graph():
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

    def add_Edge(self,node1,node2):
        self.__tableList[node1].append(node2)
        self.__tableList[node2].append(node1)
        self.__edge += 1


if __name__ == '__main__':
    graph = Graph(5)
    graph.add_Edge(0, 1)
    graph.add_Edge(2, 3)
    graph.add_Edge(2, 4)
    graph.add_Edge(1, 3)


    edge = graph.get_EdgeSize()
    nodeList4 = graph.get_NodeList(4)
    tableList = graph.get_TableList()

    print(edge)
    print(nodeList4)
    print(tableList)