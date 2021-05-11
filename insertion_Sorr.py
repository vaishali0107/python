def insertion_sort(list):
    n = len(list);
    for i in range(1,n-1):
        value=list[i];
        j=i-1;
        while j>=0 and value<list[j]:
            list[j+1]=list[j]
            j=j-1;
            list[j+1]=value;
    return list;
            
        
res = insertion_sort([2,7,8,4,6]) 
print(res);       