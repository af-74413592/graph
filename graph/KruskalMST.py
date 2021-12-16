from graph.EdgeWeightedGraph import *
from graph.UnionFind import UnionFind
import queue

class KruskalMST():
    def __init__(self,ewg):
        self.__allEdge = []
        self.__minPriority = queue.PriorityQueue()
        self.uf = UnionFind(ewg.get_NodeSize())
        for e in ewg.get_allEdges():
            node1,node2 = e.get_Node_Pair()
            weight = e.get_Weight()
            self.__minPriority.put((weight,(node1,node2),e))

        while not self.__minPriority.empty():
            self.visit()

    def visit(self):
        weight,(node1,node2),edge = self.__minPriority.get()
        if self.uf.is_connected(node1,node2):
            return
        else:
            self.uf.union(node1,node2)
            self.__allEdge.append(edge)

    def get_Edges(self):
        return [e.get_Node_Pair() for e in self.__allEdge]

if __name__ == '__main__':
    ewg = EdgeWeightedGraph(8)
    ewg.add_Edge(4, 5, 0.35)
    ewg.add_Edge(4, 7, 0.37)
    ewg.add_Edge(5, 7, 0.28)
    ewg.add_Edge(0, 7, 0.16)
    ewg.add_Edge(1, 5, 0.32)
    ewg.add_Edge(0, 4, 0.38)
    ewg.add_Edge(2, 3, 0.17)
    ewg.add_Edge(1, 7, 0.19)
    ewg.add_Edge(0, 2, 0.26)
    ewg.add_Edge(1, 2, 0.36)
    ewg.add_Edge(1, 3, 0.29)
    ewg.add_Edge(2, 7, 0.34)
    ewg.add_Edge(6, 2, 0.40)
    ewg.add_Edge(3, 6, 0.52)
    ewg.add_Edge(6, 0, 0.58)
    ewg.add_Edge(6, 4, 0.93)

    edges = KruskalMST(ewg).get_Edges()
    print(edges)