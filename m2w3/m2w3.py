from heapq import heappush, heappop 

list_arrival=[]
with open("m2w3.txt", 'r') as f:
    for num in f:
        list_arrival.append(int(num))
        
new_list=[]
min_heap=[]
max_heap=[]
medians=[]
for x in list_arrival:
    if not max_heap: 
        heappush(max_heap, -x)
    else:
        if x <= -max_heap[0]:
            heappush(max_heap, -x)
        else:
            heappush(min_heap, x)
    if len(max_heap) - len(min_heap) == 2:
        y = -heappop(max_heap)
        heappush(min_heap, y)
    elif len(min_heap) - len(max_heap) == 2:
        z = heappop(min_heap)
        heappush(max_heap, -z)
    if len(max_heap) >= len(min_heap):
        medians.append(-max_heap[0])
    elif len(max_heap) < len(min_heap):
        medians.append(min_heap[0])
        
print(sum(medians)%10000)