def Convert(tups,dictionary): 
    dictionary

arr = [(int(x),10-int(x)) for x in input().split()]
print(*arr)
arr = sorted(arr,key=lambda ele:ele[1])
print(*arr)


arr = [('year',2017),('Age',28)]
print(dict(arr))


def func1(a,*more): 
    print('a=',a)
    print('more=',more)
    
func1(1,2,3,4,5,6)


dic = {'January':907,'February':790,'March':9913}
max_value = max(dic,key=lambda month:dic[month])
print(max_value,dic[max_value])