from graph.DiGraph import DiGraph
from graph.DirectedCycle import DirectedCycle
import queue

class DepthFirstTopoLogicalOrder():
    def __init__(self,dg):
        self.__nodeSize = dg.get_NodeSize()
        self.__marked = [False for _ in range(dg.get_NodeSize())]
        self.__reversePost = queue.LifoQueue(dg.get_NodeSize())
        self.__flag = DirectedCycle(dg).hasCycle()
        if not DirectedCycle(dg).hasCycle():
            for n in range(dg.get_NodeSize()):
                if not self.__marked[n]:
                    self.df_search(dg, n)

    def df_search(self, dg, node):
        self.__marked[node] = True
        for n in dg.get_NodeList(node):
            if not self.__marked[n]:
                self.df_search(dg, n)
        self.__reversePost.put(node)

    def get_reversePost(self):
        if not self.__flag:
            result = []
            for _ in range(self.__nodeSize):
                result.append(self.__reversePost.get())
            return result
        else:
            return "图中有环"

if __name__ == '__main__':
    dg1 = DiGraph(6)
    dg1.add_Edge(0, 2)
    dg1.add_Edge(0, 3)
    dg1.add_Edge(2, 4)
    dg1.add_Edge(3, 4)
    dg1.add_Edge(4, 5)
    dg1.add_Edge(1, 3)

    print(DepthFirstTopoLogicalOrder(dg1).get_reversePost())

    dg2 = DiGraph(5)
    dg2.add_Edge(3, 0)
    dg2.add_Edge(0, 2)
    dg2.add_Edge(2, 1)
    dg2.add_Edge(1, 0)
    dg2.add_Edge(1, 4)

    print(DepthFirstTopoLogicalOrder(dg2).get_reversePost())