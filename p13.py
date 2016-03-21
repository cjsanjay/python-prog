#Find intersection of three sorted arrays

input3 = [6, 7, 20, 80, 100]
input2 = [3, 4, 25, 30, 70, 80, 120]
input1 = [1, 5, 10, 20, 40, 80]

i=0
j=0
k=0

while i<len(input1) and j<len(input2) and k<len(input3):
    print "comparing",input1[i],input2[j],input3[k]
    if input1[i]==input2[j] and input1[i]==input3[k]:
        print input1[i]
        i=i+1
        j=j+1
        k=k+1
    else:                            
        if input1[i] <input2[j]:
            i=i+1
        else:
            if input2[j] <input1[i] and input2[j]<input3[k]:
                j=j+1
            else:
                if input3[k] <input1[i] and input3[k]<input2[j]:
                    k=k+1
                else:
                    if input1[i]==input2[j] and input1[i]<input3[k]:
                        i=i+1
                        j=j+1
                    else:
                        if input2[j]==input3[k] and input2[j]<input1[i]:
                            j=j+1
                            k=k+1
                        else:
                            i=i+1
                            k=k+1              
        
        


