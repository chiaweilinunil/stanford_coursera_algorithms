graph={}

with open('m2w2.txt', 'r') as f:
    for line in f:
        parts=line.split()
        vertex = int(parts.pop(0))
        graph[vertex]=[]
        for part in parts:
            neighbor, distance = map(int, part.split(','))
            graph[vertex].append((neighbor, distance))

processed=set()
shortest_graph={}
for vertex in graph:
    shortest_graph[vertex]=float('inf')

shortest_graph[1]=0  
while len(processed) < len(graph):   
    min_distance=float('inf')
    winning_vertex=None
    # Phase 1: Find the unprocessed vertex with the shortest known distance from the start
    for vertex in shortest_graph:
        if vertex not in processed:
            if shortest_graph[vertex] < min_distance:
                min_distance=shortest_graph[vertex]
                winning_vertex=vertex
                
    # Phase 2: Add the true winner to processed and update its neighbors
    processed.add(winning_vertex)    
    for neighbor, distance in graph[winning_vertex]:
        new_distance = shortest_graph[winning_vertex] + distance
        if new_distance < shortest_graph[neighbor]:
            shortest_graph[neighbor] = new_distance
                
target_verticex=[7,37,59,82,99,115,133,165,188,197]
for vertex in target_verticex:
    print(shortest_graph[vertex])