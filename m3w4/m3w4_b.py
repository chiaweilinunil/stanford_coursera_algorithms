import sys
sys.setrecursionlimit(10000)


FILE_PATH="m3w4_b.txt"

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
        
dict={}
def f(i, x):
    weight_i=items[i][0]
    value_i=items[i][1]
    if i == 0: # base case
        return 0
    if (i, x) in dict: # cache check
        return dict[(i, x)]
    if weight_i > x:
        result = f(i-1, x)
    else:
        result = max(f(i-1, x), f(i-1, x - weight_i) + value_i)
    dict[(i, x)] = result # store cache
    return result 
    
max_value = f(num_items, knapsack_size)

print(max_value)
      
      