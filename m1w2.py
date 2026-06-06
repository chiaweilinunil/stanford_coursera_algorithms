FILE_PATH = "m1w2_integer_list.txt"

def sort_and_count(arr):
    """Input: an array A of integers
    Output: a pair (sorted_A, inv_count)
    """
    if len(arr) <= 1:
        return (arr, 0)
    else:
        m = len(arr) // 2
        left_arr = arr[:m]
        right_arr = arr[m:]
        
        sorted_left, left_inv = sort_and_count(left_arr)
        sorted_right, right_inv = sort_and_count(right_arr)
        
        merged, split_inv = merge_and_count(sorted_left, sorted_right)
        
        total_inv= left_inv + right_inv + split_inv
        return (merged, total_inv)
    
    
def merge_and_count(left_arr, right_arr):
    i = 0
    j = 0 
    merged = []
    count_inv = 0
    while i < len (left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
            count_inv += len(left_arr) - i
    
    while i < len(left_arr):
        merged.append(left_arr[i])
        i += 1
    while j < len (right_arr):
        merged.append(right_arr[j])
        j += 1
        
    return (merged, count_inv)

def main():
    with open(FILE_PATH) as f:
        arr = [int(line) for line in f]

    sorted_arr, total_inv = sort_and_count(arr)
    print(total_inv)

if __name__ == "__main__":
    main()