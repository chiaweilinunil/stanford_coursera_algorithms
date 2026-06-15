import heapq

FILE_PATH_1 = 'm4w1_a.txt'
FILE_PATH_2 = 'm4w1_b.txt'
FILE_PATH_3 = 'm4w1_c.txt'

def read_file(file_path):
    graph=dict()
    with open (file_path, 'r') as f:
        line1=f.readline()
        line1=line1.split()
        num_vertices = int(line1[0])
        num_edges = int(line1[1])
        for line in f:
            line = line.split()
            u = int(line[0])
            v = int(line[1])
            length = int(line[2])
            if u not in graph:
                graph[u] = [(v, length)]
            else:
                graph[u].append((v, length))
        print("number of vertices:", num_vertices)
        print("number of edges:", num_edges)
        assert len(graph) == num_vertices, "number of vertices not equal to number of vertices in the graph!" 
    return num_vertices, num_edges, graph

def bellman_ford(num_vertices, graph):
    dist = [0] * (num_vertices + 1)
    for _ in range(num_vertices):
        for u in graph:
            for v, length in graph[u]:
                if dist[u] + length < dist[v]:
                    dist[v] = dist[u] + length
    for u in graph:
        for v, length in graph[u]:
            if dist[u] + length < dist[v]:
                print("Negative cycle detected!")
                return None
    return dist

def reweight(graph, dist):
    new_graph=dict()
    for u in graph:
        for v, length in graph[u]:
            new_length = length + dist[u] - dist[v]
            if u not in new_graph:
                new_graph[u] = [(v, new_length)]
            else:
                new_graph[u].append((v, new_length))
    return new_graph

def dijkstra(num_vertices, graph):
    dist_dijkstra=dict()
    for src in range(1, num_vertices+1):  
        # Min-heap (priority queue) storing pairs of (distance, node)
        priority_queue = []
        inf = float('inf')
        dist = [inf] * (num_vertices + 1)

        # Distance from source to itself is 0
        dist[src] = 0
        heapq.heappush(priority_queue, (0, src))
        
        # Process the queue until all reachable vertices are finalized
        while priority_queue:
            d, u = heapq.heappop(priority_queue)
            # If this distance not the latest shortest one, skip it
            if d > dist[u]:
                continue

            # Explore all neighbors of the current vertex
            for v, w in graph[u]:
            # If we found a shorter path to v through u, update it
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(priority_queue, (dist[v], v))
        dist_dijkstra[src] = dist
        # Return the final shortest distances from the source
    return dist_dijkstra

def get_shortest_path(num_vertices, dist_dijkstra, dist_bellman_ford):
    inf = float('inf')
    real_dist = dict()
    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            if dist_dijkstra[u][v] != inf:
                real = dist_dijkstra[u][v] - dist_bellman_ford[u] + dist_bellman_ford[v]
                real_dist[(u, v)] = real
            
    return real_dist

def johnson(num_vertices, num_edges, graph):

    dist_bellman_ford = bellman_ford(num_vertices, graph)
    if dist_bellman_ford is None: # check if negative cycle exists
        print("there is a negative cycle")
        return None
    reweighted_graph = reweight(graph, dist_bellman_ford)
    dist_dijkstra = dijkstra(num_vertices, reweighted_graph)
    shortest_paths = get_shortest_path(num_vertices, dist_dijkstra, dist_bellman_ford)
    return shortest_paths
    
def main():
    n1, m1, graph1 = read_file(FILE_PATH_1)
    n2, m2, graph2 = read_file(FILE_PATH_2)
    n3, m3, graph3 = read_file(FILE_PATH_3)
    shortest_paths_1 = johnson (n1, m1, graph1)
    shortest_paths_2 = johnson (n2, m2, graph2)
    shortest_paths_3 = johnson (n3, m3, graph3)
    results = [shortest_paths_1, shortest_paths_2, shortest_paths_3]
    valid = [min(r.values()) for r in results if r is not None]
    answer = min(valid) if valid else "NULL"
    print("answer: ", answer)
    
if __name__ == "__main__":
    main()
