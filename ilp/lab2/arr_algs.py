def find_min(arr):
    min = arr[0]
    for a in arr:
        if a < min:
            min = a
    return  min

def find_mean(arr):
    sum = 0
    for a in arr:
        sum += a
    return sum / len(arr)

print(find_min([3,5,-11,10]))
print(find_mean([1,2,5,-1]))