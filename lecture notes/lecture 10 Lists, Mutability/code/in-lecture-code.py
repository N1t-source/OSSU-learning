# L1 = ['re']
# L2 = ['mi']
# L3 = ['do']
# L4 = L1 + L2
# L3.append(L4)
# print(L3)
# L = L1.append(L3)
# print(L)

# def make_ordered_list (n):
#     n = abs(n)
#     list = []
#     for i in range(n+1):
#         list.append(i)
#     return list

# v = make_ordered_list(10)
# print(v)

# def remove_element(L,e):
#     mylist = []
    
#     for i in range(len(L)) :
#         if L[i] == e:
#             pass
#         else:
#             mylist.append(L[i])
#     return mylist

# list1 = [1,2,2,3,4,5]
# e = 3
# v = remove_element(list1,e)
# print(v)


# def count_words(sen):
#     words = sen.split(' ')
#     return len(words)

# v = count_words("Hello it's me")
# print(v)

def sort_words(sen):
    mylist = sen.split(' ')
    mylist = list(mylist)
    mylist.sort()
    return mylist

v = sort_words("look at this photograph")
print(v)