import random 

FILE_PATH='m1w4.txt'

def create_graph(file_path):
    graph={}

    with open(file_path) as f: 
        for line in f:
            numbers = line.split()
            numbers=[int(number) for number in numbers]
            vertex = numbers[0]
            neighbors = numbers[1:]
            graph[vertex] = neighbors
    return graph

# get edges from graph
def get_edges(graph):
    edges=[]
    for vertex in graph:
        for neighbour in graph[vertex]:
            if vertex < neighbour:
                edges.append((vertex, neighbour))
    return edges

# randomly choose an edge
def random_choose_edge(edges):
    chosen_edge = random.choice(edges)
    return chosen_edge 

# contract the edges

def contract_edges(chosen_edge, edges):
    contracted_edges=[]
    u, v = chosen_edge 
    for vertex, neighbour in edges:
        if vertex == v:
            contracted_edges.append((u, neighbour))
        elif neighbour == v:
            contracted_edges.append((vertex, u))
        else:
            contracted_edges.append((vertex, neighbour))
    return contracted_edges

# remove self-loops
def remove_self_loops(edges):
    edges = [edge for edge in edges if edge[0] != edge[1]]
    return edges 

def count_active_vertices(edges):
    active_vertices=[]
    for a, b in edges:
        active_vertices.append(a)
        active_vertices.append(b)
    num_active_vertices=len(set(active_vertices))
    return num_active_vertices

def min_cut_counter(file_path):
    graph=create_graph(file_path)
    edges=get_edges(graph)
    num_active_vertices=count_active_vertices(edges)
    while num_active_vertices > 2:
        chosen_edge=random_choose_edge(edges)
        edges=contract_edges(chosen_edge, edges)
        edges=remove_self_loops(edges)
        num_active_vertices=count_active_vertices(edges) 
    
    print(f"min_cut:{len(edges)}")
    return len(edges)
    
def main():
    min_cuts=[]
    for _ in range (1000):
        min_cut=min_cut_counter(FILE_PATH)
        min_cuts.append(min_cut)
    
    print(min(min_cuts))
    
    
if __name__== "__main__":
    main()
        