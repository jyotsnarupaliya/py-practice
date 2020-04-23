import sys

def rotateArray(arr, positions):
    rotated_arr = [-sys.maxsize] * len(arr)
    
    for i in range(len(arr)):
        rotated_arr[i-positions] = arr[i]
        
    return rotated_arr
    
    
def rotateArray1(arr, positions):
    rotated_arr = []
    
    rotated_arr.extend(arr[positions:])
    rotated_arr.extend(arr[:positions])
    
    return rotated_arr
    

print(rotateArray1([1,2,3,4,5,6], 2))
