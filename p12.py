array=[1,2,3,9,4]

min1=array[0]
min2=array[0]

for i in range(1,len(array)):
    if array[i]<min1:       
        min1=array[i]

min2=min1

min1=1000
for i in range(len(array)):        
    if array[i]<min1 and array[i]!=min2:
        min1=array[i]

print min1            
