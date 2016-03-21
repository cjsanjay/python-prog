tasks=['A','A','D','A']

k=3
wt={}
for each_task in tasks:
    wt[each_task]=[0,0]

clock=0    
for each_task in tasks:
    if wt[each_task][0]!=0:
        if wt[each_task][0]-(clock-wt[each_task][1])<=0:
            clock=clock+1
            wt[each_task][0]=3
            wt[each_task][1]=clock
        else:
            clock=clock+(wt[each_task][0]-(clock-wt[each_task][1]))
            wt[each_task][0]=3
            wt[each_task][1]=clock    
    else:
        wt[each_task][0]=3        
        clock=clock+1
        wt[each_task][1]=clock

print clock        
