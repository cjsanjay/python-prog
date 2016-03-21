
#Merge two sorted arrays into third one
arr1 = [[3,11],[17,25],[58,73]]
arr2 = [[6,18],[40,47]]

i=0
j=0
temp=[]    
while i<len(arr1) and j<len(arr2):  
    t=[]     
    if arr1[i][0]<arr2[j][0]:
        t.append(arr1[i][0])
        t.append(arr1[i][1])
        i=i+1
    else:
        t.append(arr2[j][0])
        t.append(arr2[j][1])            
        j=j+1
    temp.append(t)

if i<len(arr1):
    while i<len(arr1):
        t=[]
        t.append(arr1[i][0])
        t.append(arr1[i][1])
        temp.append(t) 
        i=i+1
if j<len(arr2):
    while j<len(arr2):
        t=[]
        t.append(arr2[j][0])
        t.append(arr2[j][1])
        temp.append(t) 
        j=j+1       

final_temp=[]
t=[]
t.append(temp[0][0])
t.append(temp[0][1])
for i in range(1,len(temp)):
    if t[1]>temp[i][0]:
        t[1]=temp[i][1]
    else:
        final_temp.append(t)
        t=[]
        t.append(temp[i][0])    
        t.append(temp[i][1])  
        
final_temp.append(t)
print final_temp        
        
                    
    
        
