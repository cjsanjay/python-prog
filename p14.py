#find minimum value which can't be sum of any given sub array

def findMin(input1):
    min1=1
    for i in range(len(input1)):
        if input1[i]>min1:
            return min1          
        else:
            min1=min1+input1[i]      

    return min1        

input1=[1, 1, 1, 1]
print findMin(input1)
