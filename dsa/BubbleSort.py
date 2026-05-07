arr=[6,7,8,3,0,-3,-4,-9]
n=len(arr)

for i in range(n-1):       #starts from 0 t0 n-1 
    swapped=False          #because we consider that the array is already sorted which save us time complexity
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:       #its like if index of arr[0] > arr[0+1]
            arr[j],arr[j+1]=arr[j+1],arr[j]     #simple swap
            swapped=True  #means it needed to be swapped
    if not swapped:  # if not Flase
         print(f"{arr} is already sorted")
         break #to prevent from running multiple
    print(arr)
