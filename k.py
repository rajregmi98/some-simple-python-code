def _sum(arr):
    sum = 0 
    for i in arr:
        sum = sum + i 
    return (sum)

arr = []
arr=[5,3,5,9]
n = len(arr)
ans = _sum(arr)
print("sum of the array is ", ans)
