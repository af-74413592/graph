class DiGraph():
    def __init__(self,nodeSize):
        self.__nodeSize = nodeSize
        self.__edge = 0
        self.__tableList = [ [] for _ in range(self.__nodeSize)]
        self.__reverseList = [ [] for _ in range(self.__nodeSize)]

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
        self.__reverseList[node2].append(node1)
        self.__edge += 1

    def reverse(self):
        rg = DiGraph(self.__nodeSize)
        rg.__tableList = self.__reverseList
        rg.__reverseList = self.__tableList
        rg.__edge = self.__edge
        return rg

if __name__ == '__main__':
    dg = DiGraph(5)
    dg.add_Edge(0, 1)
    dg.add_Edge(2, 3)
    dg.add_Edge(2, 4)
    dg.add_Edge(1, 3)

    print(dg.get_TableList())
    rg = dg.reverse()
    print(rg.get_TableList())