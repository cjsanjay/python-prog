
#Objective: Write a function to find all the combinations of three numbers that sum to zero

  
def checkFor(start,val,array):
      memo={}
      data=[]
      temp=[]
      for i in range(start,len(array)):        
        if val-array[i] in memo:
            temp.append(array[i])
            temp.append(val-array[i])           
            data.append(temp)
            temp=[]
        else:
            memo[array[i]]=val-array[i]
      return data         

array=[2, 3, 1, -2, -1, 0, 2, -3, 0]

array=sorted(array)

for i in range(len(array)):
    d=checkFor(i+1,-array[i],array)
    for each_d in d:
        print array[i],each_d
