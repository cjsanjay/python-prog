# Enter your code here. Read input from STDIN. Print output to STDOUT
def getMinCandy(child,i,count):    
    start=1
    end=len(child)
    candy=[1 for x in range(len(child))]
    flag=0
    for i in range(start,end):
        if child[i]>child[i-1]:
            if flag!=1:
                candy[i]=candy[i-1]+1
            else:
                candy[i]+=1
        else:
            if child[i]!=child[i-1]:                
                candy[i]=min(2,candy[i-1]-1)
            if candy[i]<1:               
                flag=1
                i=i-1
    
    sum1=0       
    for each_c in candy:                 
        sum1+=int(each_c)
    print child    
    print candy    
    return sum1

num=int(raw_input())
child=[]
for i in range(num):
    child.append(int(raw_input()))
print getMinCandy(child,0,0)

    

    
