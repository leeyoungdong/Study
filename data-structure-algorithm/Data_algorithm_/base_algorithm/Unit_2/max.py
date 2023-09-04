def find_max(a, n):

    if n ==1: 
        return a[0]
    
    max_n_1 = find_max(a, n-1) 

    if max_n_1 > a[n - 1]:          
        return max_n_1      
      
    else:
        return a[n - 1]
    
a = [1,2,3,4,5,6,7,8]

print(find_max(a,len(a)))