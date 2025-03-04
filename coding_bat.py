# def front_back(str):
#     empty = []
#     newstr = ""
#     for i in str:
#         empty.append(i)
#     empty[0] = str[-1]
#     empty[-1] = str[0]
#     for i in empty:
#         newstr += i
#     return newstr
#
# #print(front_back(""))



# # def missing_char(str, n):
# #     empty = ""
# #     if len(str) >= 2:
# #         for i in range(0, len(str)):
# #             if i == n: continue
# #             else:
# #                 empty += str[i]
# #         return empty
# #     else: return str
# def missing_char(str, n):
#     return (str[:n] + str[n+1:])
#
# print(missing_char('kitten', 1))



# #Warmup-1 > parrot_trouble
# def parrot_trouble(talking, hour):
#     print("Given Solution: ", (talking and (hour < 7 or hour > 20)))
#     if not talking: return False
#     if hour < 7 or hour > 20:
#         print(hour, " is less than 7")
#         return True
#     #if hour >= 7 and hour <= 20: return False
#     else:
#         print("unhandled condition, hour is: ", hour)
#         return False # this i had as return true and that was what was failing for 7 and 20
#
# print(parrot_trouble(True, 6))
# print(parrot_trouble(True, 7))
# parrot_trouble(True, 20)

# #Warmup-1 > makes10
# def makes10(a, b):
#     #return(a == 10  or b ==10 or a+b == 10) # One-liner solution
#     if a == 10 or b == 10: # originally was 'a or b == 10'  and a was true by itself.
#     #if (a or b) == 10: # if (a or b) == 10: does not work either.
#         print(a,"== 10: ", (a == 10))
#         print(b,"== 10: ", (b == 10))
#         print(a, "== 10 or", b, "== 10:", (a == 10 or b == 10))
#         return True
#     if (a + b) == 10:
#         print("a + b == 10:", (a + b == 10))
#         return True
#     else: return False
#
# print(makes10(9,10))
# print("should be false:", (makes10(9, 9)))
# print("should be false:", (makes10(8, 3)))

# # Warmup-1 > pos_neg
# # My Code:
# def pos_neg(a, b, negative):
#     if a > 0 and b > 0: return False
#     if negative:
#         if a < 0 and b < 0 : return True
#         else: return False
#     if a > 0 and b < 0 and negative == False: return True
#     if a < 0 and b > 0 and negative == False: return True
#     #if a < 0 and b < 0 and negative == True: return True
#     if a < 0 and b < 0 and negative == False: return False
#
# # Solution:
# def pos_neg(a, b, negative):
#     if negative:
#         return (a < 0 and b < 0)
#     else:
#         return ((a < 0 and b > 0) or (a > 0 and b < 0))





# 2/10/2025
# def missing_char(str, n):
#     #del(str[n])
#     #return str
#     s = ""
#     for i in range(len(str)):
#     #for i in str:
#         if i != n:
#             s += str[i]
#     return s
#
# # # shown solution:
# # def missing_char(str, n):
# #     front = str[:n]   # up to but not including n
# #     back = str[n+1:]  # n+1 through end of string
# #     return front + back
#
# print(missing_char('kitten', 1))

# def front_back(str):
#     a = str[0]
#     s = ""
#     if len(str) > 2:
#         b = str[-1]
#         c = str[1:-1]
#
#     s += b
#     s += c
#     s += a
#     #str[0] = b
#     #str[-1] = a
#     return (s)

# def front_back(str):
#     if len(str) <= 1: # from shown solution
#         return str # from shown solution
#     a = str[0]
#     b = str[1:-1]
#     c = str[-1]
    #return str[len(str)-1] + b + str[0] # works
    # return str[len(str)-1] + b + a # works
    #return c + b + a # works
    #str[0] = b
    #str[-1] = a
    # return (c, b, a) # outputs ('e', 'od', 'c')('a', '', 'a')('b', '', 'a')
    # return (c + b + a) # works
    # return b # returns middle of string as expected
    # return str[c + b + a] # TypeError: string indices must be integers, not 'str'
    # return [c + b + a] # returns ['eodc']a['ba']
    #return str[str[-1] + str[1:-1] + str[0]] # TypeError: string indices must be integers, not 'str'
    # return str[-1] + str[1:-1] + str[0] # works
    #return str(str[-1] + str[1:-1] + str[0]) # TypeError: 'str' object is not callable
    # return (str[-1] + str[1:-1] + str[0]) # works

# # outputs:
# # ('e', 'od', 'c')
# # ('a', '', 'a')
# # ('b', '', 'a')

# def front_back(str):
#     if len(str) > 1:
#         s = ""
#         s += str[-1]
#         s += str[1:-1]
#         s += str[0]
#         return s
#     else: return str
#
# # shown solution:
# def front_back(str):
#     if len(str) <= 1:
#         return str
#     mid = str[1:len(str)-1]  # can be written as str[1:-1]
#     # last + mid + first
#     return str[len(str)-1] + mid + str[0]

# #shortest:
# def front_back(str):
#     if len(str) <= 1: return str
#     return str[-1] + str[1:-1] + str[0]
#
#
# print(front_back('code'))
# print(front_back('a'))
# print(front_back('ab'))
# print(front_back(''))

# # first attempt
# def front3(str):
#     if len(str) < 3: return str * 3
#     return str[0:3] * 3

# # revision
# def front3(str):
#     if len(str) > 3: str = str[0:3]
#     return str * 3

# # Shown Solution:
# def front3(str):
#     # Figure the end of the front
#     front_end = 3
#     if len(str) < front_end:
#         front_end = len(str)
#     front = str[:front_end]
#     return front + front + front
#
#     # Could omit the if logic, and write simply front = str[:3] # their notes
#     # since the slice is silent about out-of-bounds conditions. # their notes

# # Shortest:
# def front3(str): return str[0:3] * 3
#
# print(front3('Java'))
# print(front3('Chocolate'))
# print(front3('aBc'))
# print(front3('12'))