# board = [
#     [1,2,3,],
#     [4,'X',6],
#     [7,8,9]
# ]
# listvar=[]
# for row in board:
#     for elem in row:
#         x = tuple(row)
#         print(x,end='')
#     print()
#
# sample = [1,2,3,4,5,6,7,8,9]
# for move in sample:
#     move -= 1
#     row = move // 3 	# cell's row
#     col = move % 3		# cell's column
#     print(row,col)
#
#
# # Nested Print, list sort and tuple sorted
#
# a = 1
# b = 2
# c = 3
# # print("first print", print(b, print(c, end=""), "second", end=""),a, end="")
# lis=["a","b","c","A","C","B"]
# tup=(2,"jill"),(1,"jack")
# tup2=1,2,3,4,5,4,3,1,2
# #
# lis.sort()
# sil = lis.sort()
# print(sil)
# print(lis.sort())
# print(lis)
# print(sorted(tup))
# print(sorted(tup2))


import math
for name in dir(math):
    print(name, end="\t")