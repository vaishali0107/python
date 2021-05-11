def selection_sort(list):
    n = len(list);
    for i in range(0,n-1):
        min=i;
        for j in range(i+1,n-1):
            if list[min]>list[j]:
                min=j;
        temp = list[j];
        list[j]=list[i];
        list[i]=temp;
    return list;

res = selection_sort([34,56,23,67]); 
print(res)           