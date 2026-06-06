FILE_PATH = "m3w3_c.txt"
weights={}
mwis={}
with open (FILE_PATH, 'r') as f:
    num_vertices = int(f.readline())
    for i, line in enumerate(f, 1):
        weights[i] = int(line)

mwis[0]=0
mwis[1]=weights[1]
num_vertices=len(weights)

for i in range(2, num_vertices + 1):
    mwis[i] = max(mwis[i-1], mwis[i-2] + weights[i])

max_weight=mwis[num_vertices] 
print("max weight: ", max_weight)


# walk back and see which vertices were chosen
i = num_vertices
selected_vertices=[]
while i >= 2:
    if mwis[i] == mwis[i-2] + weights[i]:
        selected_vertices.append(i)
        i -= 2
    else: 
        i-=1
if i == 1:
    selected_vertices.append(i) 

list=[1, 2, 3, 4, 17, 117, 517, 997]
answer=[]
for v in list:
    if v in selected_vertices:
        answer.append(1)
    else:
        answer.append(0)
        
print("answer: ", answer)
