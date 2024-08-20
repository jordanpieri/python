def front_back(str):
    empty = []
    newstr = ""
    for i in str:
        empty.append(i)
    empty[0] = str[-1]
    empty[-1] = str[0]
    for i in empty:
        newstr += i
    return newstr

#print(front_back(""))



# def missing_char(str, n):
#     empty = ""
#     if len(str) >= 2:
#         for i in range(0, len(str)):
#             if i == n: continue
#             else:
#                 empty += str[i]
#         return empty
#     else: return str
def missing_char(str, n):
    return (str[:n] + str[n+1:])

print(missing_char('kitten', 1))