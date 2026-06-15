FILE_PATH="m3w2_b.txt"
MAX_DISTANCE = 3

class UnionFind:
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size))
        self.cluster_size=[1] * size
    def find(self, i):
      
        # Pass 1: climb to the root
        self.root=i
        if self.parent[i] == self.root:
            self.root=self.parent[self.root]
        
        while self.parent[self.root] != self.root:
            self.root = self.parent[self.root]

        # Pass 2: re-point everything on the path straight to root
        while self.parent[i] !=  self.root:
            self.next=self.parent[i]
            self.parent[i] =self.root
            i = self.next
        
        return self.root
    
    def unite(self, i, j):
        
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        if irep == jrep:
            return None
        
        # attach the SMALLER tree under the LARGER tree's root
        if self.cluster_size[irep] < self.cluster_size[jrep]:
            self.parent[irep] = jrep
            self.cluster_size[jrep] += self.cluster_size[irep] 
        else:
            self.parent[jrep] = irep
            self.cluster_size[irep] += self.cluster_size[jrep]




nodes=[]
bitmasks={}
with open (FILE_PATH, 'r') as f:
    line_1=f.readline()
    line_1 = line_1.split()
    num_nodes = int(line_1[0])
    num_bits = int(line_1[1])
    uf = UnionFind(num_nodes)
    for i, line in enumerate(f):
        line=line.split()
        bits=''.join(line)
        nodes.append(bits)
        bitmask = int(bits, 2)
        if bitmask in bitmasks:
            uf.unite(i, bitmasks[bitmask])
        bitmasks[bitmask] = i


for bitmask, node_id in bitmasks.items():
    for i in range (num_bits): # look for distance-1 node
        neighbour = bitmask ^ (1 << i)
        if neighbour in bitmasks:
            uf.unite(node_id, bitmasks[neighbour])
        
        
    for i in range (num_bits): # look for distance-2 node
        for j in range(num_bits): 
            neighbour = bitmask ^ (1 << i) ^ (1 << j) 
            if neighbour in bitmasks:
                uf.unite(node_id, bitmasks[neighbour])   

roots = set(uf.find(i) for i in range(num_nodes))
k = len(roots)
print(k)