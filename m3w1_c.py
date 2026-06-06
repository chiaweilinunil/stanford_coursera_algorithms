FILE_PATH="m3w1_c.txt"
X=set()
graph=dict()
total_cost=0
with open (FILE_PATH, 'r') as f:
    line_1=f.readline().split()
    number_of_nodes = int(line_1[0])
    number_of_edges = int(line_1[1])
    for line in f:
        line=line.split()
        vertex1 = int(line[0])
        vertex2 = int(line[1])
        edge_cost = int(line[2])
        if vertex1 not in graph:
            graph[vertex1] =[(vertex2, edge_cost)]
        else:
            graph[vertex1].append((vertex2, edge_cost))
        if vertex2 not in graph:
            graph[vertex2]=[(vertex1, edge_cost)]
        else:
            graph[vertex2].append((vertex1, edge_cost))

start_vertex = next(iter(graph))
X.add(start_vertex)        
while len(X) < len(graph):
    min_edge = None 
    for u in X:
        for (v, cost) in graph[u]:
            if v not in X:
                if min_edge == None:
                    min_edge = cost
                    best_vertex=v
                elif cost < min_edge:
                    min_edge = cost
                    best_vertex=v
    X.add(best_vertex)
    total_cost += min_edge
                    
print(total_cost)
                    
                 
        