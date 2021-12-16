from graph.EdgeWeightedGraph import EdgeWeightedGraph
import queue

class PrimMST():
    def __init__(self,ewg):
        # 索引代表顶点，值表示当前顶点和最小生成树之间的最短边
        self.__minEdge = [None for _ in range(ewg.get_NodeSize())]
        # 索引代表顶点，值表示当前顶点和最小生成树之间的最短边的权重
        self.__minWeight = [10000.0 for _ in range(ewg.get_NodeSize())]
        # 索引代表顶点，如果当前顶点已经在树中，则值为true，否则为false
        self.__marked = [False for _ in range(ewg.get_NodeSize())]
        # 存放树中顶点与非树中顶点之间的有效横切边
        self.__minPriority = queue.PriorityQueue()

        self.__minWeight[0] = 0.0
        self.__minPriority.put((0.0,0))

        while not self.__minPriority.empty():
            self.visit(ewg)

    def visit(self,ewg):
        nodeWeight,node = self.__minPriority.get()
        if self.__minWeight[node] >= nodeWeight:
            self.__marked[node] = True
            for e in ewg.get_TableList()[node]:
                other = e.get_Node_Either(node)
                if self.__marked[other]:
                    continue
                if e.get_Weight()< self.__minWeight[other]:
                    self.__minEdge[other] = e
                    self.__minWeight[other] = e.get_Weight()
                    self.__minPriority.put((e.get_Weight(),other))

    def get_Edges(self):
        return [ e.get_Node_Pair() for e in self.__minEdge[1:]]


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

    edges = PrimMST(ewg).get_Edges()
    print(edges)