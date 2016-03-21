

def heapifyUp(heap,i):
    if i==0:
        return heap
    else:
        parent=i/2
        if heap[parent]>heap[i]:
            temp=heap[parent]
            heap[parent]=heap[i]
            heap[i]=temp
            heap=heapifyUp(heap,parent)
        return heap        

def heapifyDown(heap,parent):
    lchild=parent*2
    rchild=(parent*2)+1
    pos=-1
    if lchild<len(heap) and rchild<len(heap):
        if heap[rchild]<heap[lchild]:
            pos=rchild
        else:
            pos=lchild
    else:
        if rchild<len(heap):
            pos=rchild
        if lchild<len(heap):
            pos=lchild            
    if pos==-1:
        return heap
    else:
        if heap[parent]>heap[pos]:
            temp=heap[pos]
            heap[pos]=heap[parent]
            heap[parent]=temp
            heapifyDown(heap,pos)
            return heap
        else:
            return heap    
                                        
                        


def insert(ch,heap):
    heap.append(ch)
    heap=heapifyUp(heap,len(heap)-1)
    return heap

str1="cccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrxfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtabababababcccddrfgghtababababab"
str2="ddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtabaxbcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccabababddrfgghtababcccababab"
heap=[]
heap1=[]
for i in range(len(str1)):
    heap=insert(str1[i],heap)
    
for i in range(len(str2)):
    heap1=insert(str2[i],heap1)
        
print str1    
print str2
while len(heap)>0 and len(heap1)>0:
   if heap[0]==heap1[0]:
    cur=heap.pop()
    cur1=heap1.pop()
    if len(heap)>=1 and len(heap1)>=1:      
        heap[0]=cur
        heap1[0]=cur1
        heap=heapifyDown(heap,0)
        heap1=heapifyDown(heap1,0)
   else:
    print "Not Anagram"
    break

if len(heap)==0 and len(heap1)==0:
    print "Anagram"
else:
    print "Not Anagram"         
