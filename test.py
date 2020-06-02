# New change
def arrlist(lst,k=0):
    if k==5: 
        print('popped')
        x=lst.pop()
        return 
    lst.append(k+5)
    print('array before : ', *lst)
    arrlist(lst,k+1)
    print('array after : ', *lst)
    if len(lst) > 0: 
        x=lst.pop()
        x = x + 2
    return 
    
    
arrlist([])
