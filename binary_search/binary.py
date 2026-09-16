arr = [10,20,30,40,50,60,70,80,90,100]
target = 0
start =0
end =len(arr)-1
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
        print("Found")
        break
    elif arr[mid] < target:
        start = mid +1
    else:
        end = mid -1
return -1