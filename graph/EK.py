from graph.EdgeWeightedDigraph import *
import queue

class EK():
    def __init__(self, graph, start,end):
        self.__residual = [[0 for _ in range(graph.get_NodeSize())] for _ in range(graph.get_NodeSize())]
        # 残余图的剩余流量
        self.__maxflowgraph = [[0 for _ in range(graph.get_NodeSize())] for _ in range(graph.get_NodeSize())]
        self.__pre = [-1 for _ in range(graph.get_NodeSize())]
        self.__flow = [0.0 for _ in range(graph.get_NodeSize())]
        self.__waitSearch = queue.Queue()
        for e in ewdg.get_allEdges():
            s,t = e.get_Node_Pair()
            weight = e.get_Weight()
            self.__residual[s][t] = weight
        self.maxflow(graph,start,end)

    def bf_search(self,graph,start,end):
        self.__flow[start] = float('inf')
        self.__waitSearch.put(start)
        while not self.__waitSearch.empty():
            w = self.__waitSearch.get()
            if w == end:
                break
            for n in range(graph.get_NodeSize()):
                if ((n != start)) and (self.__residual[w][n]>0) and (self.__pre[n] == -1):
                    self.__pre[n] = w
                    self.__flow[n] = min(self.__flow[w],self.__residual[w][n])
                    self.__waitSearch.put(n)
        if (self.__pre[end] == -1):
            # 汇点的前驱还是初始值，说明已无增广路径
            return -1
        else:
            return self.__flow[end]

    def maxflow(self,graph,start,end):
        sumflow = 0  # 记录最大流，一直累加
        while(True):
            augmentflow = self.bf_search(graph,start,end)
            if (augmentflow == -1):
                break
            k = end
            end = self.__pre[end]
            while (k != start):  # k回溯到起点，停止
                prev = self.__pre[k]  # 走的方向是从prev到k
                self.__maxflowgraph[prev][k] += augmentflow
                self.__residual[prev][k] -= augmentflow  # 前进方向消耗掉了
                self.__residual[k][prev] += augmentflow  # 反向边
                k = prev
            sumflow += augmentflow
        print(sumflow)

    def get_maxflowgraph(self):
        return self.__maxflowgraph

if __name__ == '__main__':
    ewdg = EdgeWeightedDigraph(6)
    ewdg.add_Edge(0, 1, 0.3)
    ewdg.add_Edge(0, 2, 0.2)
    ewdg.add_Edge(1, 2, 0.1)
    ewdg.add_Edge(1, 3, 0.3)
    ewdg.add_Edge(1, 4, 0.4)
    ewdg.add_Edge(2, 4, 0.2)
    ewdg.add_Edge(3, 5, 0.2)
    ewdg.add_Edge(4, 5, 0.3)

    print(EK(ewdg,0,5).get_maxflowgraph())