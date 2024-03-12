import numpy as np 

lst1 = [10,20,30,40,50] 
lst2 = [1,2,3,4,5]


vctr1 = np.array(lst1) 

vctr2= np.array(lst2) 


print("Vector created from a list 1:") 
print(vctr1) 
print("Vector created from a list 2:") 
print(vctr2) 

vctr_add = vctr1+vctr2
print("Addition of two vectors: ",vctr_add)