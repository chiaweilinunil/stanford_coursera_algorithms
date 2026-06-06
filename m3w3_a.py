import heapq 
FILE_PATH='m3w3_a.txt'
symbols=[]
with open (FILE_PATH, 'r') as f:
    num_symbols=int(f.readline())
    for line in f:
        weight=int(line)
        symbols.append((weight, 0))


heapq.heapify(symbols) 
while len(symbols) > 1:
    first = heapq.heappop(symbols)
    second = heapq.heappop(symbols)
    new_weight = first[0] + second[0]
    new_depth = max(first[1], second[1]) +1
    new_nod=(new_weight, new_depth)
    heapq.heappush(symbols, new_nod)

max_depth = symbols[0][1]
print(max_depth)
    


