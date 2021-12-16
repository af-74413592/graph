from graph.Graph import Graph
import queue

class BreadthFirstSearch():
    def __init__(self, graph, node):
        self.__marked = [False for _ in range(graph.get_NodeSize())]
        self.__count = 0
        self.__waitSearch = queue.Queue()
        self.bf_search(graph, node)

    def bf_search(self,graph,node):
        self.__marked[node] = True
        self.__waitSearch.put(node)
        while not self.__waitSearch.empty():
            w = self.__waitSearch.get()
            for n in graph.get_NodeList(w):
                if not self.__marked[n]:
                    self.__marked[n] = True
                    self.__waitSearch.put(n)
            self.__count += 1

    def get_Marked(self,node):
        return self.__marked[node]

    def get_Count(self):
        return self.__count

if __name__ == '__main__':
    graph = Graph(13)
    graph.add_Edge(0, 5)
    graph.add_Edge(0, 1)
    graph.add_Edge(0, 2)
    graph.add_Edge(0, 6)
    graph.add_Edge(5, 3)
    graph.add_Edge(5, 4)
    graph.add_Edge(3, 4)
    graph.add_Edge(4, 6)
    graph.add_Edge(7, 8)
    graph.add_Edge(9, 11)
    graph.add_Edge(9, 10)
    graph.add_Edge(9, 12)
    graph.add_Edge(11, 12)

    bfs = BreadthFirstSearch(graph,0)
    count = bfs.get_Count()
    print("与起点0相通的顶点的数量为:{}",count)
    marked1 = bfs.get_Marked(5)
    marked2 = bfs.get_Marked(7)
    print("顶点5和顶点0是否相通:{}",marked1)
    print("顶点7和顶点0是否相通:{}",marked2)