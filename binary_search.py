def binary_search(array,key,n):
    low=0
    high=n-1;
    while(low<=high):
        mid = int((low+high)/2);
        if(array[mid]==key):
            return mid;
        elif(array[mid]>key):
            high = mid+1;
        elif(array[mid]<key):
            low=mid-1;
        else:
            return -1;
    
    
array =[10,20,30,40,50,60,70];
key = 10;
n = len(array);
res = binary_search(array,key,n)
if(res==-1):
    print("Element not found");
else:
    print("Element is present at index",res)