# def div_by(n,d):
#     #so n and d are ints > 0
#     # returns true if d divides n evenly else false
#     if n < 0 or d< 0 :
#         print(f"You can't divide Zero")
#     else:
#         return n%d == 0

# print(div_by(10,3))
# print(div_by(195,13))

def is_palindrome(s):
    s = str(s)
    rev = s[::-1]
    if s  == rev:
        print(f"This is word [{rev}] is a Palindrome")
    else:
        print(f"This is word [{rev}] is not a Palindrome of {s}")
is_palindrome('abcd')