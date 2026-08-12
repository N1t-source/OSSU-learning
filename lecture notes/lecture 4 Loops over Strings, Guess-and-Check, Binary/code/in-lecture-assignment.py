# range(5),range(10),range(2,9,3),range(-4,6,2),range(5,6)


# def loop(start,end=0,step=0):
#   even_counter = 0
#   if end == 0 and step ==0 :
#     for i in range(start):
#           if i == 0 and i % 2 == 0:
#              even_counter += 0
#           else:
#              if i !=0 and i % 2 == 0:
#               even_counter +=1
#   else:
#     if end == 0 :
#       for i in range(0,end=start,step=step):
#         if i == 0 and i % 2 == 0:
#           even_counter += 0
#         else:
#             if i !=0 and i % 2 == 0:
#               even_counter +=1
#     elif step == 0 :
#        for i in range(start,end):
#           if i == 0 and i % 2 == 0:
#               even_counter += 0
#           else:
#             if i !=0 and i % 2 == 0:
#               even_counter +=1
#     else:
#        for i in range(start,end,step):
#             if i == 0 and i % 2 == 0:
#              even_counter += 0
#             else:
#              if i !=0 and i % 2 == 0:
#               even_counter +=1
#   print(f"Even numbers:{even_counter}")

# state = loop(5,6)


# s = 'abca'
# counter = 0
# container = ''
# for char in s :
#  if char not in container:
#      container += char
#      counter +=1
# print(f"Counts {counter}")


hardcode = 3
for value in range(1,11):
    if value == hardcode:
        print(f'Found vaule:{value}')
        break
    else:
        print(f'Value NOT Found:{value}')