FILE_PATH="m3w2_a.txt"
SIZE = 500 
nodes=[]
with open (FILE_PATH, 'r') as f:
    line_1=f.readline()
    num_nodes = int(line_1)
    for line in f:
        line=line.split()
        node_1=int(line[0])
        node_2=int(line[1])
        cost=int(line[2])
        nodes.append((node_1, node_2, cost))

nodes.sort(key=lambda x: x[2])

class UnionFind:
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size + 1))
    
    def find(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
          
        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])
    
    def unite(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep


num_clusters = SIZE
uf = UnionFind(SIZE)

for (n1,n2, cost) in nodes:

    if uf.find(n1) != uf.find(n2):
        if num_clusters == 4:
            max_spacing = cost
            break 
        uf.unite(n1, n2)
        num_clusters -= 1
    else:
        continue
    
print(max_spacing)