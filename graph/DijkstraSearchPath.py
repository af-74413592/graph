from graph.EdgeWeightedDigraph import *
import queue

class DijkstraSearchPath():
    def __init__(self,ewdg,start):
        # 索引代表顶点，值表示从顶点s到当前顶点的最短路径上的最后一条边
        self.__lastEdge = [None for _ in range(ewdg.get_NodeSize())]
        # 索引代表顶点，值从顶点s到当前顶点的最短路径的总权重
        self.__allWeight = [10000.0 for _ in range(ewdg.get_NodeSize())]
        # 存放树中顶点与非树中顶点之间的有效横切边
        self.__minPriority = queue.PriorityQueue()
        self.__allWeight[start] = 0.0
        self.__minPriority.put((0.0,start))
        while not self.__minPriority.empty():
            self.relax(ewdg)

    def relax(self,ewdg):
        nodeWeight, node = self.__minPriority.get()
        for edge in ewdg.get_NodeList(node):
            end = edge.get_End_Node()
            weight = edge.get_Weight()
            # 通过松弛技术，判断从起点s到顶点e的最短路径是否需要先从顶点s到顶点n，然后再由顶点n到顶点e
            if (self.__allWeight[node] + weight < self.__allWeight[end]):
                self.__allWeight[end] = self.__allWeight[node] + weight
                self.__lastEdge[end] = edge
                self.__minPriority.put((weight,end))

    def get_allWeight(self,end):
        return self.__allWeight[end]

    def has_PathTo(self,end):
        return self.__allWeight[end] < 10000.0

    def pathTo(self,end):
        if not self.has_PathTo(end):
            return None
        allEdges = []

        while True:
            edge = self.__lastEdge[end]
            if edge == None:
                break
            allEdges.append(edge)
            end = edge.get_Start_Node()

        return [edge.get_Node_Pair() for edge in reversed(allEdges)]

if __name__ == '__main__':
    ewdg = EdgeWeightedDigraph(8)
    ewdg.add_Edge(4, 5, 0.35)
    ewdg.add_Edge(5, 4 ,0.35)
    ewdg.add_Edge(4, 7 ,0.37)
    ewdg.add_Edge(5, 7 ,0.28)
    ewdg.add_Edge(7, 5 ,0.28)
    ewdg.add_Edge(5, 1 ,0.32)
    ewdg.add_Edge(0, 4 ,0.38)
    ewdg.add_Edge(0, 2 ,0.26)
    ewdg.add_Edge(7, 3 ,0.39)
    ewdg.add_Edge(1, 3 ,0.29)
    ewdg.add_Edge(2, 7 ,0.34)
    ewdg.add_Edge(6, 2 ,0.40)
    ewdg.add_Edge(3, 6 ,0.52)
    ewdg.add_Edge(6, 0 ,0.58)
    ewdg.add_Edge(6, 4 ,0.93)


    print(DijkstraSearchPath(ewdg,0).pathTo(6))