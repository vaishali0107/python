def linear_search(array,key,n):
   
    for i in range (0,n):
        if(array[i]==key):
            return i;
    return -1;
        
        

array = [5,10,20,30,65,35,45]
key= 35;
n = len(array);

"""res = linear_search(array,key,n)"""
res=linear_search([23,45,76,34,26],76,5)
if (res == -1):
    print("Key is not present");
else:
    print("Key is gound at index",res);    
    

