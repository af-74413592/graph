from graph.Graph import Graph

def Hungarian(l_node,visited):
    for r_node in graph.get_NodeList(l_node):
        if r_node not in T:
            S[l_node] = r_node
            T[r_node] = l_node
            return True
        else:
            l_next_node = T[r_node]
            if l_next_node not in visited:
                visited.add(l_next_node)
                if Hungarian(l_next_node, visited):
                    S[l_node] = r_node
                    T[r_node] = l_node
                    return True
    return False

if __name__ == '__main__':
    graph = Graph(10)
    graph.add_Edge(0,5)
    graph.add_Edge(0,6)
    graph.add_Edge(0,7)
    graph.add_Edge(1,5)
    graph.add_Edge(1,6)
    graph.add_Edge(1,8)
    graph.add_Edge(1,9)
    graph.add_Edge(2,6)
    graph.add_Edge(2,7)
    graph.add_Edge(3,6)
    graph.add_Edge(3,7)
    graph.add_Edge(4,8)
    graph.add_Edge(4,9)
    S,T = {},{}
    for l_node in range(5):
        Hungarian(l_node,visited=set())
        print(S)