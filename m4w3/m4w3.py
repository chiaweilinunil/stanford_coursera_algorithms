import math

FILE_PATH = "m4w3.txt"

def read_file(file_path):
    coords={}
    with open(file_path, 'r') as f:
        line_1 = f.readline()
        num_city = int(line_1)
        for line in f:
            line = line.split()
            index = int(line[0])
            x = float(line[1])
            y = float(line[2])
            coords[index] = (x, y)
    return num_city, coords

def squared_euclidean(coord1, coord2):
    x = coord1[0]
    y = coord1[1]
    z = coord2[0]
    w = coord2[1]
    distance = (x-z)**2  + (y-w)**2
    return distance

def find_closest_city(start, coords):
    closest_city = float('inf')
    closest_dist = float('inf')
    for i, coord in coords.items():
        dist = squared_euclidean(start, coord) 
        if dist < closest_dist:
            closest_city = i
            closest_dist = dist
        elif dist == closest_dist:
            if i < closest_city: 
                closest_city = i
            else:
                continue
    return closest_city, closest_dist

def visit_closest_city(coords):
    start_coord = coords[1]
    current_coord = coords[1]
    del coords[1]
    total_dist = 0
    while coords: 
        closest_city, closest_dist = find_closest_city(current_coord, coords)
        total_dist += math.sqrt(closest_dist)
        current_coord = coords[closest_city]
        del coords[closest_city]
    
    final_step = math.sqrt(squared_euclidean(start_coord, current_coord))
    total_dist += final_step

    return math.floor(total_dist)

def traveling_salesman_problem(file_path):
    _ , coords = read_file(file_path)
    total_dist = visit_closest_city(coords)
    return total_dist

total_dist = traveling_salesman_problem(FILE_PATH)
print("answer: ", total_dist)
        
    
    
    