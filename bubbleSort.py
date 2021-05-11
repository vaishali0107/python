def Bubble_sort(array):
    n = len(array);
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j];
    return array;  

res = Bubble_sort([3,5,8,9,4]) ;
print(res);         
                
                
                