from collections import deque, defaultdict
import math
import random

FILE_PATH_1 ="m4w4_a.txt"
FILE_PATH_2 ="m4w4_b.txt"
FILE_PATH_3 ="m4w4_c.txt"
FILE_PATH_4 ="m4w4_d.txt"
FILE_PATH_5 ="m4w4_e.txt"
FILE_PATH_6 ="m4w4_f.txt"

def read_file(file_path):
    clauses=[]
    with open(file_path, 'r') as f:
        line_1 = f.readline()
        n = int(line_1)
        for line in f:
            line = line.split()
            x = int(line[0])
            y = int(line[1])
            clauses.append((x, y))
    return n, clauses # structure [(1,2), (3, 4)]
             
def build_index(clauses):
    variables = defaultdict(list)
    pos_count = defaultdict(int)
    neg_count = defaultdict(int)
    for i, (x, y) in enumerate(clauses):
        variables[abs(x)].append(i)
        variables[abs(y)].append(i)
            
        if x > 0:
            pos_count[x] += 1
        else: 
            neg_count[abs(x)] += 1
        if y > 0:
            pos_count[y] += 1
        else: 
            neg_count[abs(y)] += 1
            
    return variables, pos_count, neg_count # structure: {variable: [clause_id_1, clause_id_2.....]}

def is_pure(variable, pos_count, neg_count): # helper function 
    return pos_count[variable] == 0 or neg_count[variable] == 0

def elimination_loop(clauses, variables, pos_count, neg_count):
    q = deque()
    for v, _ in variables.items():
        if is_pure(v, pos_count, neg_count): # check purity
            q.append(v)
    
    # elimination loop  
    removed = [False] * len(clauses)      
    while q:
        v = q.popleft()
        for clause_id in variables[v]:
            if removed[clause_id]:
                continue
            removed[clause_id] = True
            x, y = clauses[clause_id] # remove the other variable in the clause
            other = y if abs(x) == v else x # another variable
            u = abs(other)
            if other > 0:
                pos_count[u] -= 1
            else:
                neg_count[u] -= 1
                
            if is_pure(u, pos_count, neg_count):
                q.append(u)
    
    updated_clauses = []
    for clause_id in range(len(clauses)):
        if not removed[clause_id]:
            updated_clauses.append(clauses[clause_id])
    
    return updated_clauses

    
class Papadimitriou():
    def __init__(self, clauses):
       self.clauses = clauses
       variables , _, _ = build_index(clauses)
       self.variables = variables
       self.k = len(self.variables)
    
    def clause_is_satisfied(self, x, y, values): # check if a clause is satisfied or not 
        return values[abs(x)] == (x > 0) or values[abs(y)] == (y > 0) 
    
    def inner_loop(self):
        
        num_inner_loop = 2 * self.k ** 2 
        
        values = {v: bool(random.getrandbits(1)) for v in self.variables}
        unsatisfied_clauses = {clause_id for clause_id, (x, y) in enumerate(self.clauses) if not self.clause_is_satisfied(x, y, values)}
  
        for _ in range(num_inner_loop):
            if not unsatisfied_clauses:
                return True 
            clause_id = next(iter(unsatisfied_clauses))
            x, y =self.clauses[clause_id]
            flipped_variable = abs(random.choice((x, y)))
            values[flipped_variable] = not values[flipped_variable]
            for id in self.variables[flipped_variable]:
                a, b = self.clauses[id]
                if self.clause_is_satisfied(a, b, values):
                    unsatisfied_clauses.discard(id)
                else:
                    unsatisfied_clauses.add(id)
        
        return False
                
               
    def outer_loop(self):
        num_outer_loop = math.log(self.k, 2)
        for _ in range(int(num_outer_loop)):
            if self.inner_loop():
                return True
        return False


def solve_one_file(file_path):
    n, clauses = read_file(file_path)
    variables, pos_count, neg_count = build_index(clauses)
    updated_clauses = elimination_loop(clauses, variables, pos_count, neg_count)
    print(f"{file_path}: core size = {len(updated_clauses)}")
    
    if not updated_clauses:
        satisfied = True
    else: 
        alg = Papadimitriou(updated_clauses)
        satisfied = alg.outer_loop()
    print("answer: ", satisfied)
    return 1 if satisfied else 0 

solve_one_file(FILE_PATH_1)
solve_one_file(FILE_PATH_2)
solve_one_file(FILE_PATH_3)
solve_one_file(FILE_PATH_4)
solve_one_file(FILE_PATH_5)
solve_one_file(FILE_PATH_6)