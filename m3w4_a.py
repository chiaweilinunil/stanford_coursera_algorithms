FILE_PATH="m3w4_a.txt"
with open(FILE_PATH, 'r') as f:
    line_1=f.readline()
    knapsack_size=int(line_1[0])
    num_items=int(line_1[1])
    for line in f:
        value=int(line[0])
        weight=int(line[1])