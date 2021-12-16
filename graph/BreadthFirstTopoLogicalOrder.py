from graph.DiGraph import DiGraph
from graph.DirectedCycle import DirectedCycle
import queue

class BreadthFirstTopoLogicalOrder():
    def __init__(self,dg):
        self.__dgList = dg.get_TableList()
        self.__bgList = dg.reverse().get_TableList()
        self.__nodeSize = dg.get_NodeSize()
        self.__marked = [False for _ in range(dg.get_NodeSize())]
        self.__reversePost = queue.LifoQueue(dg.get_NodeSize())
        self.__flag = DirectedCycle(dg).hasCycle()
        if not DirectedCycle(dg).hasCycle():
            self.kahn()

    def kahn(self):
        while not self.__reversePost.full():
            for i in range(len(self.__dgList)):
                if not self.__dgList[i]:
                    if not self.__marked[i]:
                        self.__reversePost.put(i)
                        self.__marked[i] = True
                        for n in self.__bgList[i]:
                            self.__dgList[n].remove(i)

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

    print(BreadthFirstTopoLogicalOrder(dg1).get_reversePost())

    dg2 = DiGraph(5)
    dg2.add_Edge(3, 0)
    dg2.add_Edge(0, 2)
    dg2.add_Edge(2, 1)
    dg2.add_Edge(1, 0)
    dg2.add_Edge(1, 4)

    print(BreadthFirstTopoLogicalOrder(dg2).get_reversePost())