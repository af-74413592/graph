from graph.Graph import Graph
import queue

class BreadthFirstPaths():
    def __init__(self, graph, node):
        self.__marked = [False for _ in range(graph.get_NodeSize())]
        self.__start = node
        self.__edgeTo = [-1 for _ in range(graph.get_NodeSize())]
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
                    self.__edgeTo[n] = w
                    self.__waitSearch.put(n)

    def has_PathTo(self,node):
        return self.__marked[node]

    def path_To(self,node):
        if not self.has_PathTo(node):
            return None
        else:
            path = [node]
            while node != self.__start:
                node = self.__edgeTo[node]
                path.append(node)
            path.reverse()
        return path

if __name__ == '__main__':
    graph = Graph(6)
    graph.add_Edge(0,2)
    graph.add_Edge(0,1)
    graph.add_Edge(2,1)
    graph.add_Edge(2,3)
    graph.add_Edge(2,4)
    graph.add_Edge(3,5)
    graph.add_Edge(3,4)
    graph.add_Edge(0,5)

    bfp = BreadthFirstPaths(graph,0)
    path = bfp.path_To(4)
    print(path)