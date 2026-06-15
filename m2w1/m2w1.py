from collections import defaultdict, Counter 

FILE_PATH="m2w1.txt"
G = defaultdict(list)
G_rev = defaultdict(list)
n=875714
with open(FILE_PATH, 'r') as f:
    for line in f:
        u, v = map(int, line.split())
        G[u].append(v)
        G_rev[v].append(u)

explored=[False] * (n+1)
f_values=[0] *(n+1)
t = 0
s = None 
leader=[0] * (n+1)
order_by_f=[0] * (n+1)

def pass1():
    global t 
    t = 0
    global s
    s = None
    for i in range(n, 0, -1):
        if explored[i] == False:
            s = i
            DFS(G_rev, i)
    for v in range(1, n+1):
        order_by_f[f_values[v]] = v

    
def pass2():
    global explored
    explored = [False] * (n+1)
    global t
    t = 0
    global s
    s = None
    for k in range(n, 0, -1) :
        i = order_by_f[k]
        if explored[i] == False:
            s = i
            DFS(G, i)

def DFS(graph, i):
    stack=[(i, False)]
    while stack:
        v, is_finish = stack.pop() 
        if is_finish == True:
            global t 
            t += 1
            f_values[v] = t
        if explored[v] == True:
            continue
        explored[v]=True
        leader[v]=s
        stack.append((v, True))
        for j in graph[v]:
            if explored[j]==False:
                stack.append((j, False))

        
pass1()
pass2()

counts=Counter(leader[1:])
sizes=sorted(counts.values(), reverse=True)
print(sizes[:5])