#-----------minimum and maximum value

arr=[0,12,3,5,-1,20,-100]

min_value=arr[0]
max_value=arr[0]

for value in arr:
    if value<=min_value:
        min_value=value
print(min_value)

for value in arr:
    if value>=max_value:
        max_value=value
print(max_value)  