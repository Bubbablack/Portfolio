
def combine(lst1, lst2): 
    return [sub[item] for item in range(len(lst2)) 
                      for sub in [lst1, lst2]] 
 

print(combine([1,2,3], [11,22,33]))