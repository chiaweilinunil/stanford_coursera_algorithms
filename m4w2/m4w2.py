import math
from itertools import combinations

FILE_PATH = 'm4w2.txt'

def read_file(file_path):
    coords=[]
    with open(file_path, 'r') as f:
        line_1 = f.readline()
        num_city = int(line_1)
        for line in f:
            line = line.split()
            x = float(line[0])
            y = float(line[1])
            coords.append((x, y))
    return num_city, coords

def euclidean(coord1, coord2):
    x = coord1[0]
    y = coord1[1]
    z = coord2[0]
    w = coord2[1]
    distance = math.sqrt((x-z)**2  + (y-w)**2)
    return distance

def build_distance_matrix(num_city, coords):
    distances=[[0.0] * num_city for _ in range(num_city)]
    for city1 in range(num_city):
        
        for city2 in range(num_city):
            distance=euclidean(coords[city1], coords[city2])
            distances[city1][city2] = distance
    return distances
        

def travaling_salesman_problem(num_city, distances):
    prev = dict()
    inf = float('inf')
    # base case
    prev[1] = {0: 0.0}
        
    for m in range (2, num_city + 1): # loop through the subproblems
        curr = dict()
        for group in combinations(range(1, num_city), m-1): # loop through subset of S
            S = 1
            for i in group: 
                S |= (1 << i) # bit representation of the traversed cities
            curr[S] = dict()
            for j in group:
                best = inf
                S_without_j = S & ~(1 << j)
                for k in (0,) + group:
                    if k != j: 
                        prev_cost = prev[S_without_j].get(k, inf)
                        best = min (best, prev_cost + distances[k][j])
                curr[S][j] = best
        prev = curr    

    full = (1 << num_city) -1  # bit mask representation of the full set  
    best = inf
    for c in range(1, num_city):        
        best = min(best, curr[full][c] + distances[c][0])
        
    return math.floor(best) 

def main():
    num_city, coords=read_file(FILE_PATH)
    distances = build_distance_matrix(num_city, coords)
    answer = travaling_salesman_problem(num_city, distances)
    print(answer)
    
if __name__ == "__main__":
    main()