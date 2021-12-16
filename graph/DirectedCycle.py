from graph.DiGraph import DiGraph

class DirectedCycle():
    def __init__(self,dg):
        self.__marked = [False for _ in range(dg.get_NodeSize())]
        self.__hasCycle = False
        self.__onStack = [False for _ in range(dg.get_NodeSize())]

        for n in range(dg.get_NodeSize()):
            if not self.__marked[n]:
                self.df_search(dg, n)

    def df_search(self, dg, node):
        self.__marked[node] = True
        self.__onStack[node] = True
        for n in dg.get_NodeList(node):
            if not self.__marked[n]:
                self.df_search(dg, n)
            if self.__onStack[n]:
                self.__hasCycle = True
                return
        self.__onStack[node] = False

    def hasCycle(self):
        return self.__hasCycle

if __name__ == '__main__':
    dg1 = DiGraph(5)
    dg1.add_Edge(0, 1)
    dg1.add_Edge(2, 3)
    dg1.add_Edge(2, 4)
    dg1.add_Edge(1, 3)
    print(DirectedCycle(dg1).hasCycle())
    dg2 = DiGraph(5)
    dg2.add_Edge(3, 0)
    dg2.add_Edge(0, 2)
    dg2.add_Edge(2, 1)
    dg2.add_Edge(1, 0)
    dg2.add_Edge(1, 4)
    print(DirectedCycle(dg2).hasCycle())