from graph.DiGraph import *
import numpy as np

class PageRank():
    def __init__(self,dg,q=0.85):
        self.q = q                 # q为阻尼系数
        self.graph = dg
        self.max_iterations = 100  # 最大迭代次数
        self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
        self.NodeSize = dg.get_NodeSize()

        #初始化得分矩阵 给每个节点赋予初始的PR值
        self.PrScore = np.ones(self.NodeSize)/ self.NodeSize
        self.reverseList = dg.reverse().get_TableList()
        self.page_rank()

    def page_rank(self):
        # 先将图中没有出链的节点改为对所有节点都有出链
        for i in range(self.NodeSize):
            if len(self.graph.get_NodeList(i)) == 0:
                for j in range(self.NodeSize):
                    self.graph.add_Edge(i,j)
        damping_value = (1.0 - self.q) / self.NodeSize  # 公式中的(1−q)/N部分

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in range(self.NodeSize):
                rank = 0
                for r in self.reverseList[node]:  # 遍历所有“入射”的页面
                    rank += self.q * (self.PrScore[r] / len(self.graph.get_NodeList(r)))
                rank += damping_value
                change += abs(self.PrScore[node] - rank)  # 绝对值
                self.PrScore[node] = rank

            print("This is NO.%s iteration" % (i + 1) )
            print(self.PrScore)

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("finished in %s iterations!" % (i + 1))
        else:
            print("finished out of 100 iterations!")

        print(sum(self.PrScore))

if __name__ == '__main__':
    dg = DiGraph(5)
    dg.add_Edge(0, 1)
    dg.add_Edge(2, 3)
    dg.add_Edge(2, 4)
    dg.add_Edge(1, 3)

    PageRank(dg)
