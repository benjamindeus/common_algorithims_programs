# searching algorithim
# linear search
"""
    This is a linear search operation done on python
    this has a constant complexity
"""
def linear_search(list,target):
    if len(list) > 0:
        for i in range(0,len(list)-1):
            if list[i] == target:
                return list[i]
        return None

data =[22,34,1,34,21,44,56,2,34,555,33,14,4,56,88,97,43]
target = 188

def verify(list,target):
    runnner = linear_search(list=list,target=target)
    if runnner:
        print("The target found %s"%runnner)
    else:
        print("Target not found")

verify(list=data,target=target)