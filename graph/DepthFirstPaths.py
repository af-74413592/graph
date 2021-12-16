from graph.Graph import Graph

class DepthFirstPaths():
    def __init__(self, graph, node):
        self.__marked = [False for _ in range(graph.get_NodeSize())]
        self.__start = node
        self.__edgeTo = [-1 for _ in range(graph.get_NodeSize())]
        self.df_search(graph, node)

    def df_search(self,graph,node):
        self.__marked[node] = True
        for n in graph.get_NodeList(node):
            if not self.__marked[n]:
                self.__edgeTo[n] = node
                self.df_search(graph,n)

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

    dfp = DepthFirstPaths(graph,0)
    path = dfp.path_To(4)
    print(path)