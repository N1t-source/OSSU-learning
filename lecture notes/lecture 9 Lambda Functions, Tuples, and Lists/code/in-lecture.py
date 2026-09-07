# def char_counts(s):
#     vowels = 'aeiou'
#     f_element = 0
#     s_element = 0
#     for char in s:
#         if char in vowels:
#             f_element += 1
#         else:
#             s_element += 1
#     return  f_element,s_element
        
# word = char_counts('word')
# print(word)


def sum_and_prod(l):
    sum = 0
    prod = 1
    for i in l:
        sum += i
        prod *= i 
    return sum, prod

sum_prod = sum_and_prod((1,2,5,3,5,7,8,9))
print(sum_prod)