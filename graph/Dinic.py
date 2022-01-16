from graph.EdgeWeightedDigraph import *
import queue


class Dinic():
    def __init__(self, graph, start,end):
        self.__nodesize = graph.get_NodeSize()
        self.__residual = [[0 for _ in range(self.__nodesize)] for _ in range(self.__nodesize)]
        # 残余图的剩余流量
        self.__maxflowgraph = [[0 for _ in range(self.__nodesize)] for _ in range(self.__nodesize)]
        self.__pre = [-1 for _ in range(self.__nodesize)]
        self.__flow = [0.0 for _ in range(self.__nodesize)]
        self.__level = [-1 for _ in range(self.__nodesize)]
        self.__sumflow = 0
        self.__waitSearch = queue.Queue()
        for e in ewdg.get_allEdges():
            s,t = e.get_Node_Pair()
            weight = e.get_Weight()
            self.__residual[s][t] = weight
        self.dinic(start,end)

    def build_level(self,start,end):
        # 根据残余图来构建层次图,过程类似无权最短路径
        self.__level[start] = 0 #源点的层次为0
        level_pre = [-1 for _ in range(self.__nodesize)]
        #BFS地寻找增广路径
        self.__waitSearch.put(start)
        while not self.__waitSearch.empty():
            w = self.__waitSearch.get()
            for n in range(self.__nodesize):
                if(n == start or n==w):
                    continue
                if(self.__residual[w][n]>0 and level_pre[n] == -1):
                    # 只要能往下走且没有被标记过
                    level_pre[n] = w
                    # 标记前驱，也代表已构造了层次
                    self.__level[n] = self.__level[w] + 1
                    # 层次逐渐加1
                    self.__waitSearch.put(n)
                    # 加入队列
        print('层次图为',self.__level)
        if (level_pre[end] != -1):
            # 如果构造层次图能构造到汇点，说明有增广路径
            return True
        else:
            return False

    def get_augment(self,start,end):
        # 根据层次图，构造可能的增广路径
        self.temp_augment = [start]
        # 每条增广路径都是从源点开始的
        count = 1 #源点下一层的层次为1
        self.recursion(count,start,end)

    def recursion(self,count,start,end):
        for i in range(self.__nodesize):
            if(self.__level[i] == count):#寻找层次为count的点
                self.temp_augment.append(i)
                if(i==end):
                    # 找到了一条可能的增广路径
                    print('可能的增广路径', self.temp_augment)
                    self.send_flow(start, end)
                self.recursion(count + 1,start,end)  # 寻找下一层次的点
                self.temp_augment.remove(i)

    def send_flow(self,start,end):
        augment = self.temp_augment
        self.__flow[end] = float('inf')#设为无穷，且以这个作为找到增广路径的标志
        print('初始flow', self.__flow)
        for i in range(len(augment)-1):
            self.__flow[augment[i+1]] = min(self.__flow[augment[i]],self.__residual[augment[i]][augment[i+1]])
            print('行进增广路径过程中的flow', self.__flow)
        if(self.__flow[end] !=0 ):
            # flow[sink]不为0，说明增广路径有效
            self.__sumflow += self.__flow[end]
            print('有效的增广路径', augment, self.__flow)
            for i in range(len(augment) - 1):
                # 对残余图和最大流图的相应修改
                self.__residual[augment[i]][augment[i + 1]] -= self.__flow[end]
                self.__residual[augment[i + 1]][augment[i]] += self.__flow[end]
                self.__maxflowgraph[augment[i]][augment[i + 1]] += self.__flow[end]

    def dinic(self,start,end):
        self.__flow[start] = float('inf')
        while(True):
            temp = self.build_level(start,end)
            if not temp:
                print(self.__sumflow)
                break
            else:
                self.get_augment(start,end)

    def get_maxflowgraph(self):
        return self.__maxflowgraph

if __name__ == '__main__':
    ewdg = EdgeWeightedDigraph(6)
    ewdg.add_Edge(0, 1, 1.0)
    ewdg.add_Edge(0, 2, 1.0)
    ewdg.add_Edge(1, 2, 0.2)
    ewdg.add_Edge(1, 3, 0.4)
    ewdg.add_Edge(1, 4, 0.8)
    ewdg.add_Edge(2, 4, 0.9)
    ewdg.add_Edge(4, 3, 0.6)
    ewdg.add_Edge(3, 5, 1.0)
    ewdg.add_Edge(4, 5, 1.0)

    print(Dinic(ewdg,0,5).get_maxflowgraph())