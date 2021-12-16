from graph.EdgeWeightedDigraph import *
import numpy as np

class FloydSearchPath():
    def __init__(self,ewdg):
        self.__NodeSize = ewdg.get_NodeSize()
        # 保存到达目标顶点的前驱节点和最后一条边
        self.__lastEdge = [[[] for _ in range(self.__NodeSize)] for _ in range(self.__NodeSize)]
        # 索引代表顶点，值从顶点s到各个顶点的距离(邻接矩阵)
        self.__allDistance = np.empty((self.__NodeSize,self.__NodeSize))
        # 初始化邻接矩阵
        self.__allDistance.fill(10000.0)
        for table in ewdg.get_TableList():
            for edge in table:
                start = edge.get_Start_Node()
                end = edge.get_End_Node()
                weight = edge.get_Weight()
                self.__allDistance[start][start] = 0.0
                self.__allDistance[start][end] = weight
                self.__lastEdge[start][end] = edge
        self.floyd()

    def floyd(self):
        # k为中间节点的下标
        for k in range(self.__NodeSize):
            # i为开始节点的下标
            for i in range(self.__NodeSize):
                # j为结束节点的下标
                for j in range(self.__NodeSize):
                    # 计算以k为中间节点，i为开始节点，j为结束节点，i->k->j的距离
                    distance = self.__allDistance[i][k] + self.__allDistance[k][j]
                    # 如果i->j的距离大，则更新距离表和前驱节点表
                    if distance < self.__allDistance[i][j]:
                        self.__allDistance[i][j] = distance
                        self.__lastEdge[i][j] = self.__lastEdge[i][k]

    def get_allDistance(self):
        return self.__allDistance

    def has_PathTo(self,start,end):
        return self.__allDistance[start][end] < 10000.0

    def pathTo(self,start,end):
        if not self.has_PathTo(start,end):
            return None
        edgeList = []
        while True:
            edge = self.__lastEdge[start][end]
            if edge == []:
                break
            edgeList.append(edge)
            start = edge.get_End_Node()

        return [edge.get_Node_Pair() for edge in edgeList]

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


    print(FloydSearchPath(ewdg).pathTo(0,6))