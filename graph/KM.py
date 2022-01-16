from graph.EdgeWeightedGraph import *

def get_matrix(ewg):
    a = -float('inf')
    matrix = [ [a for _ in range(5)] for _ in range(5)]
    for e in ewg.get_allEdges():
        w = e.get_Weight()
        lnode,rnode = e.get_Node_Pair()
        if w > matrix[lnode][rnode-5]:
            matrix[lnode][rnode-5] = w
    label_left, label_right = [max(g) for g in matrix], [0 for _ in range(5)]
    return matrix,label_left,label_right

def find_path(i,matrix, visited_left, visited_right, slack_right):
    visited_left[i] = True
    for j, match_weight in enumerate(matrix[i]):
        if visited_right[j]:
            continue
        gap = label_left[i] + label_right[j] - match_weight
        if gap == 0:
            visited_right[j] = True
            if j not in T or find_path(T[j],matrix, visited_left, visited_right, slack_right):
                T[j] = i
                S[i] = j+5
                return True

        else:
            slack_right[j] = min(slack_right[j], gap)
    return False

def KM(matrix):
    m = len(matrix)
    for i in range(m):
        # 重置辅助变量
        slack_right = [float('inf') for _ in range(m)]
        while True:
            visited_left = [False for _ in matrix]
            visited_right = [False for _ in matrix]
            if find_path(i,matrix,visited_left,visited_right, slack_right):
                break
            d = float('inf')
            for j, slack in enumerate(slack_right):
                if not visited_right[j] and slack < d:
                    d = slack
            for k in range(m):
                if visited_left[k]:
                    label_left[k] -= d
                if visited_right[k]:
                    label_right[k] += d
    return S, T

if __name__ == '__main__':

    ewg = EdgeWeightedGraph(10)
    ewg.add_Edge(0, 5, 0.4)
    ewg.add_Edge(0, 6, 0.2)
    ewg.add_Edge(0, 7, 0.6)
    ewg.add_Edge(1, 5, 0.2)
    ewg.add_Edge(1, 6, 0.6)
    ewg.add_Edge(1, 8, 0.6)
    ewg.add_Edge(1, 9, 0.3)
    ewg.add_Edge(2, 6, 0.3)
    ewg.add_Edge(2, 7, 0.6)
    ewg.add_Edge(3, 6, 0.8)
    ewg.add_Edge(3, 7, 0.2)
    ewg.add_Edge(4, 8, 0.3)
    ewg.add_Edge(4, 9, 0.1)

    matrix, label_left, label_right = get_matrix(ewg)
    S, T = {}, {}
    KM(matrix)
    print(S)