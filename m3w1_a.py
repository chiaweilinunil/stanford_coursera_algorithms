FILE_PATH="m3w1_a.txt"
jobs=[]
accumulated_length=0
weighted_completion_time=0
with open (FILE_PATH, 'r') as f:
    first_line = f.readline()
    for line in f:
        line=line.split()
        weight=int(line[0])
        length=int(line[1])
        jobs.append([weight, length]) 

jobs.sort(key=lambda job: (job[0] - job[1], job[0]), reverse=True)

for job in jobs:
    accumulated_length += job[1]
    weighted_completion_time += job[0] * accumulated_length

print("weighted_completion_time: ", weighted_completion_time)