# 6.1 The append method for adding items to a list
# a_list = ['a','b','c','d','e']
# print(a_list)
# a_list.append('f')
# print(a_list)


# 6.2 The extend Method for adding items to a list

# list1 = ['a','b','c']
# list2 = [1,2,3]
# list1.extend(list2)
# print(list1)
# list1.extend('d')
# print(list1)

# Difference between append and extend Functions

# extend
# list1 = [11,22,33,44]
# list1.extend([55,66])
# print(list1)

# append
# list1 = [11,22,33,44]
# list1.append([55,66])
# print(list1)


# 6.4 The insert Method for add items to a list
# slist = ['Bunthai',178.9,'John',173.5,'Jane',176.1]
# print(slist)
# slist.insert(4,"petter")
# slist.insert(5,168.1)
# print(slist)

# 6.5 remove method for deleting items from a list
# n_list = [11,22,33,44,55,66]
# print(n_list)
# n_list.remove(11)
# print(n_list)


# bts = ['doctor','bunthai','Lyeng']
# if 'doctor' in bts :
#     bts.remove('doctor')
# print(bts)


# 6.7 The pop Method for deleting the last item in the list
# n_list = [10,20,30]
# print(n_list)
#
# n=n_list.pop()
# print('n = ',n)
# print('n_list = ', n_list)

# 6.8 Deleting list item using Del keyword

# n_list = [11,22,33,44,55,66]
# print(n_list)
#
# del n_list[3]
# print(n_list)
# n_list.insert(3,45)
# print(n_list)

# 6.9 The sort Method for sorting list items

list1 = [20,10,40,50,30]
list1.sort()
print(list1)

list1.sort(reverse = True)
print(list1)