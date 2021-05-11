def merge_sort(list):
    if(len(list)>1):
        mid = len(list)//2;
        left_list = list[:mid];
        right_list = list[mid:];
        merge_sort(left_list);
        merge_sort(right_list);
        i=0;
        j=0;
        k=0;
        while i<len(left_list) and j<len(right_list):
            if(left_list[i]<right_list[j]):
                list[k]=left_list[i];
                i+=1;
                k+=1;
            else:
                list[k]=right_list[j];
                j+=1;
                k+=1;
        while i<len(left_list):
            list[k]=left_list[i];
            i+=1;
            k+=1;
        while j<len(right_list):
            list[k]=right_list[j];
            j+=1;
            k+=1;
            
            
n = int(input("How many elements you want to enter"))
list = [];
for i in range(0,n):
    element=int(input("Enter elements"));
    list.append(element);
print(list);    
merge_sort(list);
print(list);