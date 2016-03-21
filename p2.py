#rearrange to have unique value alternate to each other

from collections import Counter
string="aaaabbcc"

bag=Counter()

for each_s in string:
    bag[each_s]+=1

flag=1
temp=[]
i=-1
while flag:
    flag1=0
    for each_item in bag:        
        if bag[each_item]!=0:
            flag1=1
            i=i+1    
            temp.append(each_item)            
            bag[each_item]-=1
            if len(temp)>1:
                if temp[i]==temp[i-1]:
                    print "Not Valid"
                    flag=0
                    break
    if flag1==0:
        break                
    
if flag:
    print "Valid"                            
           
              
