def partition(arr,low,high):
    i = low-1;
    pivot = arr[high];
    for j in range(low,high):
        if(arr[j]<=pivot):
            i+=1;
            arr[j],arr[i]=arr[i],arr[j];
    arr[i+1],arr[high]=arr[high],arr[i+1];
    return i+1;


def quick_sort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
        
arr = []
n = int(input("Enter the elements"));
for i in range(0,n):
    element = int(input("Enter element"))
    arr.append(element);
    
low = 0;
high=len(arr)-1;
quick_sort(arr,low,high)
print(arr)

"""def partition(sort_list, low, high):
    i = (low -1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)
            
def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)
lst = []
size = int(input("Enter size of the list: "))
for i in range(size):
    elements = int(input("Enter an element"))
    lst.append(elements)
low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print(lst)"""            
           
            
            