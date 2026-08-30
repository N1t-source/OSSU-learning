# def bisection_root(x):
#     epsilon =0.01
#     low= 0
#     high = x
#     ans = (high + low) /2.0
#     while abs(ans**2 - x)>= epsilon:
#         if ans**2 < x:
#             low =ans
#         else:
#             high = ans
#         ans = (high + low)/2.0
#     return ans

# def count_nums_with_sqrt_close_to (n,espilon):
#     count = 0
#     for i in range(n**3):
#         sqrt = bisection_root(i)
#         if abs(n-sqrt) < espilon:
#             print(i,sqrt)
#             count += 1
#     return count
        
# print(count_nums_with_sqrt_close_to(10,0.2))

# def criteria(n):
#      return n % 2 == 0

# def apply(criteria,n):
#      ans = 0
#      for i in range(n+1):
#           ans = criteria(i)
#           print(i,':',ans)
#      return ans

# t= apply(criteria,10)