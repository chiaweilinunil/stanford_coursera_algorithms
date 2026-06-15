from bisect import bisect_left, bisect_right 

numbers=set()
all_t=set()
with open("m2w4.txt", "r") as f:
    for line in f:
        numbers.add(int(line))

numbers_sorted=sorted(numbers)
for x in numbers_sorted:
    y_lo=-10000 - x
    y_hi= 10000 - x 
    start = bisect_left(numbers_sorted, y_lo) 
    end = bisect_right(numbers_sorted, y_hi)
    for y in numbers_sorted[start:end]:
        if x != y:
            all_t.add(x+y)
            
print(len(all_t))