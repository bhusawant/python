# Q.2)

def merge(list1, list2):
    list1.extend(list2)
    return list1

def compare(list1, list2):
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False
    return True


from Mypackage.Listpackage.listops import merge, compare

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged_list = merge(list1, list2)
print("Merged list:", merged_list)

list3 = [1, 2, 3]
list4 = [4, 5, 6]

result = compare(list3, list4)
print("Result of comparison:", result)
