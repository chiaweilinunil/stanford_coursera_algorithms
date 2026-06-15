FILE_PATH="m3w4_a.txt"

items=[(0,0)]
with open(FILE_PATH, 'r') as f:
    line_1=f.readline()
    line_1=line_1.split()
    knapsack_size=int(line_1[0])
    num_items=int(line_1[1])
    for line in f:
        line=line.split()
        value=int(line[0])
        weight=int(line[1])
        items.append((weight, value))
        
A = [[0 for i in range(knapsack_size+1)] for j in range(num_items+1)]
for i in range (1, num_items + 1):
    for j in range (1, knapsack_size + 1):
        weight_i = items[i][0]
        value_i = items[i][1]
        if weight_i> j:
            A[i][j]=A[i-1][j]
        else:
            A[i][j]=max(A[i-1][j], A[i-1][j - weight_i] + value_i)
            

print(A[num_items][knapsack_size])