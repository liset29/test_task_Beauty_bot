from collections import Counter

list = [[665587, 2], [669532, 1], [669537, 2], [669532, 1], [665587, 1]]

def grouping_values(list):
    lst = Counter(map(tuple,list))
    lst = [[key,value,count] for (key,value),count in lst.items()]
    return lst

print(grouping_values(list))
