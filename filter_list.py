# remove str list data

def filter_list(l):
    newl = []
    for i in l:
        if type(i) != str:
            newl.append(i)
    return newl


list1 = [1, 2, 'a']
print(filter_list(list1))
