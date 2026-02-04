from collections import defaultdict
# Complete the countTriplets function below.
def countTriplets(arr, r):
    result = 0
    left_map = defaultdict(int)
    mid_map = defaultdict(int)
    for num in arr:
        if num % r == 0:
            second_num = num // r
            result += mid_map.get(second_num,0) 
        if num % r == 0:
            first_num = num // r
            mid_map[num] += left_map.get(first_num,0)
            
        left_map[num] += 1   
    
    return result
    