# # Testing quote and double quote printing
# print('Greg\'s book.')
# print("'Greg's book.'")
# print('"Greg\'s book."')
# print("Greg\'s book.")
# print('"Greg\'s book."')

# # Try and Except ##!!!! IMPORTANT!!!!
# anything = input("Enter a number: ")
# try:
#     n = int(anything)
# except:
#     n = int(input("Really. Enter a number: "))
# finally:
#     something = n ** 2.0
#     print(n, "to the power of 2 is", something)

# # Right Triangle hypotenuse
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)

# # I dunno
# x = float(input("Enter value for x: "))
# y = 1/(1/(1/(1/x + x) + x) + x)
# print("y =", y)

# # Duration of time spent added to current time
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
#
# # Write your code here.
# fl60 = (mins + dura) // 60
# mod60 = (mins + dura) % 60
#
# adhr = hour + fl60
# if adhr > 23:
#     adhr %= 24
# print(adhr,":",mod60,sep="")

# # Checking how modulo would answer
# print(3%4)

# # Leap Year calculator
# #year = int(input("Enter a year: "))
# years = [2000,2015,1999,1996,1580,1900,2008,2012,2016,1988]
# for year in years:
#     if year < 1582:
#         print(str(year) + " is not within the Gregorian calendar period")
#     else:
#         #  Write the if-elif-elif-else block here.
#         # if the year number isn't divisible by four, it's a common year;
#         if year % 4 != 0 : print(str(year) + " is a Common year")
#         # otherwise, if the year number isn't divisible by 100, it's a leap year;
#         elif year % 100 != 0 : print(str(year) + " is a Leap year")
#         # otherwise, if the year number isn't divisible by 400, it's a common year;
#         elif year % 400 != 0 : print(str(year) + " is a Common year")
#         # otherwise, it's a leap year.
#         else : print(str(year) + " is a Leap year")

# # multi-variable assignment
# x, y, z = 5, 10, 8
# x, y, z = z, y, x
# print(x, y, z)

# A program that reads a sequence of numbers and counts how many numbers are even and how many are odd. The program terminates when zero is entered.

# print(0 == False)  # True
# print(1 == True)   # True
# print(['zero', 'one'][False])  # is 'zero'

# 3.2.17 SECTION QUIZ
#
# for i in range(1, 11): # Line of code. # Line of code.
#     if i % 2 != 0: print(i)
# #Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:
# x = 1
# while x < 11: # Line of code. # Line of code. # Line of code.
#     if x % 2 != 0: print(x)
#     x += 1
#
# Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:
# #my solution:
# word = ""
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@": # Line of code. # Line of code.
#         break
#     else:
#         word += ch
# print(word)

# #sample solution:
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")
#
#
# # Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:
# # my solution
# for digit in "0165031806510":
#     if digit == "0": # Line of code. # Line of code. # Line of code.
#         digit = "x"
#     print(digit, end="")
# print("\n")
# # sample solution:
# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")
#
# Question 6: What is the output of the following code?
# n = range(4)
# for num in n:
#     print(num - 1)
# else: print(num)
# 3.3.2 Logical expressions
# var = 1
# # Example 1:
# print(var > 0)
# print(not (var <= 0))
#
#
# # Example 2:
# print(var != 0)
# print(not (var == 0))
#
# You may be familiar with De Morgan's laws. They say that:
# The negation of a conjunction is the disjunction of the negations.
# The negation of a disjunction is the conjunction of the negations.
# p=1
# q=1
# print(not (p and q) == (not p) or (not q)) #True
# print(not (p or q) == (not p) and (not q)) #False
# # I dont' really understand this... The instructions are unclear and the expected result is not spelled out to let me know if the True and False I printed are correct.

# # 3.3.5 How do we deal with single bits? (note- this doesn't run due to SyntaxError: invalid decimal literal
# x=1
# flag_register = 0000000000000000000000000000x000
# x & 1 = x
# print(flag_register)
# x & 0 = 0
# print(flag_register)

# # 3.4.8 Adding elements to a list: append() and insert()
#
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
#
# ###
#
# numbers.append(4)
#
# print(len(numbers))
# print(numbers)
#
# ###
#
# numbers.insert(0, 222)
# print(len(numbers))
# print(numbers)
#
# #

# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.append(i + 1)
#
# print(my_list) # prints [1, 2, 3, 4, 5]

# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.insert(0, i + 1)
#
# print(my_list) # prints [5, 4, 3, 2, 1]

# 3.4.9 Making use of lists
#
# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in range(len(my_list)):
#     total += my_list[i]
#
# print(total) # 27

# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in range(len(my_list)):
#     print(i)
#     my_list.insert(0, my_list[i])
#     total += my_list[i]
#
# print(my_list)
# print(total) # 100 is my guess - 50 was the result. I knew the list would expand to at least 10 elements but I expected the initial range value in the list to change and it does not.

# # this is me messing with the above. I wanted to make a list and have the loop expand the way [for i in range(len(my_list))] did not expand. The problem is that the list has int values which it will interpret as the location of the list as well as the value. So list item[0]=10 and then is immediately evaluated as list value[10] which did not exist. so the value of [0]=0 did make the exanding loop/list i was looking for but also created an infinite loop.
# my_list = [0, 10, 8, 3, 5]
# total = 0
#
# for i in my_list:
#     print(i)
#     my_list.insert(0, my_list[i])
#     total += my_list[i]
#
# print(my_list)

# 3.4.10 Lists in action

# my_list = [10, 1, 8, 3, 5]
#
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
#
# print(my_list)

# # Will it still be acceptable with a list containing 100 elements? No, it won't.
# #
# # Can you use the for loop to do the same thing automatically, irrespective of the list's length? Yes, you can.
# #
# # This is how we've done it:
#
# my_list = []
# for i in range(1, 101):
#     my_list.append(i)
# print(my_list)
# length = len(my_list)
# print(range(length // 2))
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
#
# print(my_list)

# 3.4.11   LAB   The basics of lists ‒ the Beatles
# # Scenario
# # The Beatles were one of the most popular music groups of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.
# #
# # The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).
# #
# #
# # Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
# #
# # step 1: create an empty list named beatles;
# # step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# # step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# # step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# # step 5: use the insert() method to add Ringo Starr to the beginning of the list.
# # By the way, are you a Beatles fan? (The Beatles is one of Greg's favorite bands. But wait...who's Greg...?)
#
# # step 1
# beatles = []
# print("Step 1:", beatles)
#
# # step 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)
#
# # step 3
# for i in range(2):
#     inp=input("prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best: ")
#     beatles.append(inp)
# print("Step 3:", beatles)
#
# # step 4
# del beatles[4]
# del beatles[3]
# print("Step 4:", beatles)
#
# # step 5
# beatles.insert(0, "Ringo Starr")
# print("Step 5:", beatles)
#
#
# # testing list length
# print("The Fab", len(beatles))

# 3.5.2 Sorting a list
# my_list = [8, 10, 6, 2, 4]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.
# swaps = 0 # my addition to get a count of the swaps
# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             swaps += 1 # my addition to get a count of the swaps
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print(my_list)
# print("Swaps:", swaps) # Swaps: 8

# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
#
# print("\nSorted:")
# print(my_list)

# # 3.6.1 The inner life of lists
# # the name of an ordinary variable is the name of its content;
# # the name of a list is the name of a memory location where the list is stored.
# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)
#
# a = [1]
# b = a
# a[0] = 2
# print(b)

# # 3.6.2 Powerful slices & 3.6.3 Slices – negative indices
# # Copying the entire list.
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)
#
# # Copying some part of the list.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# j_list0 = my_list[1:-1]
# j_list1 = my_list[1:4]
# j_list2 = my_list[0:5]
# j_list2 = my_list[0:len(my_list)]
# j_list3 = my_list[1:-2]
# j_list4 = my_list[4]
# print(new_list)
# print(j_list0)
# print(j_list1)
# print(j_list2)
# print(j_list3)
# print(j_list4)

# 3.6.5 Lists – some simple programs
# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# #largest = my_list[0]
# #largest = 0
# largest = False
#
# for i in my_list:
# #for i in my_list[:]:
#     if i > largest:
#         largest = i
#
# print(largest)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 55
# found = False
#
# for i in range(len(my_list)): # I'm not sure why they did the 'range(len(' combo for this one when it works the same with just 'my_list'. Found out- if it runs to the end of the loop the range len wont give 'list index out of range'
# #for i in my_list:
#     found = my_list[i] == to_find # this is the type of pythonic logic that still feels foreign to me. its not an if statement but its still conditional and has no error when false
#     if found:
#         break
#
# if found:
#     print("Element found at index", i) # I'm shocked that this 'i' var persisted outside the loop
# else:
#     print("absent")


# drawn = [5, 11, 9, 42, 3, 49]
# bets = [3, 7, 11, 42, 34, 49]
# hits = 0
#
# for number in bets:
#     if number in drawn:
#         hits += 1
#
# print(hits)

# 3.6.6   LAB   Operating with lists ‒ basics

# this doesn't work. missed the hint to use a placeholder list. it was really close though. probably 2 hours
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# for i in range(len(my_list)):
#     #while i < len(my_list):
#     if my_list[i] in my_list[i+1:]:
#         for j in range(1, len(my_list[i+1:-1])):
#             print(i+j)
#             if my_list[i] == my_list[i+j]:
#                 print("removing my_list[",i,"+",j,"]:",my_list[i+j],sep='')
#                 del my_list[i+j]
#                 j -= 1
#                 i -= 1
#                 print(my_list)
#     else:
#         print(i,"not in range. Current List:",my_list)
# print("The list with unique elements only:")
# print(my_list)

# # second run through failure before realization - probably 2 hours
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# placeHolder = []
# unique = False
# while unique is False:
#     i = 0
#     if my_list[i] in my_list[i+1:]:
#         print("if my_list[",i,"](",my_list[i],") in my_list[i+1:](",my_list[i+1:],")",sep='')
#         x = my_list[i]
#         for num in my_list:
#             if num == x:
#                 print("i; ", i,". num: ", num, ". x: ", x,". list before removal: ",my_list,sep='')
#                 del my_list[i]
#                 i+=1
#     else:
#         unique = True
#         placeHolder.append(my_list[i])
#         print("placeHolder:",placeHolder)
# my_list = placeHolder
# print("The list with unique elements only:")
# print(my_list)

# # Realization of the proper method. took like 2 seconds
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# placeHolder = []
#
# for x in my_list:
#     if x not in placeHolder:
#         placeHolder.append(x)
# my_list = placeHolder
# print("The list with unique elements only:")
# print(my_list)

# 3.6.8 SECTION QUIZ
# Question 2: What is the output of the following snippet?
# This surprised me. I thought the 'del list_2' would target the memory location not just that variable name

# list_1 = ["A", "B", "C"]
# list_2 = list_1
# list_3 = list_2
#
# del list_1[0]
# del list_2
#
# print(list_3)

# # Question 5: Insert in or not in instead of ??? so that the code outputs the expected result.
# my_list = [1, 2, "in", True, "ABC"]
#
# print(1 in my_list)  # outputs True
# print("A" not in my_list)  # outputs True
# print(3 not in my_list)  # outputs True
# print(False in my_list)  # outputs False

# # 3.7.1 Lists in lists
# # List comprehensions
# row = ["WHITE_PAWN" for i in range(8)]
# print(row)
# squares = [x ** 2 for x in range(10)]
# print(squares)
# twos = [2 ** i for i in range(8)]
# print(twos)
# odds = [x for x in squares if x % 2 != 0 ]
# print(odds)

# EMPTY = "EMPTY"
# ROOK = "ROOK"
# KNIGHT = "KNIGHT"
# PAWN = "PAWN"
# board = [[EMPTY for i in range(8)] for j in range(8)]
# print(board)
# board[0][0] = ROOK
# board[0][7] = ROOK
# board[7][0] = ROOK
# board[7][7] = ROOK
# board[4][2] = KNIGHT
# board[3][4] = PAWN
# print(board)

# 3.7.3 Multidimensional nature of lists: advanced applications
# temps = [[0.0 for h in range(24)] for d in range(31)]
# #
# # The matrix is magically updated here.
# #
# print(temps)
# total = 0.0
#
# for day in temps:
#     total += day[11]
#
# average = total / 31
#
# print("Average temperature at noon:", average)
#
# highest = -100.0
#
# for day in temps:
#     for temp in day:
#         if temp > highest:
#             highest = temp
#
# print("The highest temperature was:", highest)
#
# hot_days = 0
#
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
#
# print(hot_days, "days were hot.")

# rooms = [[[0 for r in range(20)] for f in range(15)] for t in range(3)]
# rooms[1][9][13] = True
# rooms[0][4][1] = False
# vacancy = 0
#
# for room_number in range(20):
#     if not rooms[2][14][room_number]:
#         vacancy += 1
# print(rooms)
# print(vacancy)

# 3.8 Module 3 Completion – Module Test
#
# # Question 9
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1
#     print(var)
#
#
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c)
# print(d)
# print(e)
# print(c + d + e)

# # Question 19
# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
# print(t)

# I got a 65% on my first try of this assessment

# # 4.3.1 Effects and results: the return instruction
# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return
#
#     print("Happy New Year!")
#
# happy_new_year()
#
# happy_new_year(False)

# 4.3.2 A few words about None
# def strange_function(n):
#     if(n % 2 == 0):
#         return True

# print(strange_function(2))
# print(strange_function(1))

# Day Month Year Labs
# # 4.3.4   LAB   A leap year: writing your own functions
#
# def is_year_leap(year):
# #
#     # if year is int: # doesn't work
#     if year % 2 == 1:
#         return False
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#
# # test_data = [1900, 2000, 2016, 1987]
# # test_results = [False, True, True, False]
# # for i in range(len(test_data)):
# #     yr = test_data[i]
# #     print(yr,"->",end="")
# #     result = is_year_leap(yr)
# #     print(yr, result)
# #     if result == test_results[i]:
# #         print("OK")
# #     else:
# #         print("Failed")
#
# # 4.3.5   LAB   How many days: writing and using your own functions
#
# def days_in_month(year, month):
#     months = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if is_year_leap(year): months[1] = 29
#     return months[month-1]
#
# # test_years = [1900, 2000, 2016, 1987]
# # test_months = [2, 2, 1, 11]
# # test_results = [28, 29, 31, 30]
# # for i in range(len(test_years)):
# #     yr = test_years[i]
# #     mo = test_months[i]
# #     print(yr, mo, "->", end="")
# #     result = days_in_month(yr, mo)
# #     if result == test_results[i]:
# #         print("OK")
# #     else:
# #         print("Failed")
#
#
# # 4.3.6   LAB   Day of the year: writing and using your own functions
#
# def day_of_year(year, month, day):
#     days = 0
#     if days_in_month(year,month) - day < 0 : return None
#     days += day
#     while month -1 > 0:
#         month -= 1
#         days += days_in_month(year, month)
#         # print()
#     return days
#
# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_day = [29,29,17,30]
# test_results = [None, 60, 17, 334]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     dy = test_day[i]
#     print(yr, mo, dy, "->", end="")
#     result = day_of_year(yr, mo, dy)
#     print(result)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# 4.3.7   LAB   Prime numbers ‒ how to find them
# def is_prime(num):
#     for j in range(num,2,-1):
#         # print(num," % (",j,"-1) = ", num % (j-1), sep="", end="\n")
#         if num % (j-1) == 0:
#             return False
#     return True
#
# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

# 4.3.8   LAB   Converting fuel consumption
# mile = 1609.344
# gallon = 3.785411784
# def liters_100km_to_miles_gallon(liters):
#     # miles per gallon is calculated by miles/gallon
#     gallons = liters / gallon
#     miles = 100 / mile
#     # print(miles, " miles / ", gallons," gallons", sep="")
#     return miles / gallons * 1000
#
#
# def miles_gallon_to_liters_100km(miles):
#     m = miles * mile
#     # print("Miles on one gallon:",miles,"is",m,"meters, which is",m / 1000,"kilometers.")
#     k = m / 1000
#     # print("1 Gallon divided into k's is",gallon / k," then * 100 ", gallon / k * 100)
#     return gallon / k * 100
#
# # print("A 5k is",5000 / mile,"miles.")
# # print("A 100k is",100 / mile,"miles.")
#
# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))
#
# # Expected output:
# #
# # 60.31143162393162
# # 31.36194444444444
# # 23.52145833333333
# # 3.9007393587617467
# # 7.490910297239916
# # 10.009131205673757

# 4.5.2 Sample functions: Triangles
# Evaluating a triangle's area

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
#
#
# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
#     if b > a and b > c:
#             return b ** 2 == a ** 2 + c ** 2
# print(is_a_right_triangle(3, 5, 4))
# print(is_a_right_triangle(1, 3, 4))

# 4.5.3 Sample functions: Factorials
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
#
#
# for n in range(1, 6):  # testing
#     print(n, factorial_function(n))

# 4.5.4 Fibonacci numbers
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
#
#
# for n in range(1, 10):  # testing
#     print(n, "->", fib(n))

# 4.5.5 Recursion
# # Fibonacci Recursion Version 1
# # def fib(n):
# #     if n < 1:
# #         return None
# #     if n < 3:
# #         return 1
# #     return fib(n - 1) + fib(n - 2)
# #
# # for n in range(1, 10):  # testing
# #     print(n, "->", fib(n))
#
# # Factorial Recursion Version 1
# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)
#
# for n in range(-1, 10):  # testing - this one works with -1, 0, 1
#     print(n, "->", factorial_function(n))
#
# # Factorial Recursion Version 2
# def factorial(n):
#     if n == 1:    # The base case (termination condition.) ## does not handle 0 and -1. this is how the course presented it
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(4)) # 4 * 3 * 2 * 1 = 24
# print(factorial(3)) # 4 * 3 * 2 * 1 = 24
# print(factorial(2)) # 4 * 3 * 2 * 1 = 24
# print(factorial(1)) # 4 * 3 * 2 * 1 = 24
# #print(factorial(0)) # 4 * 3 * 2 * 1 = 24
# #print(factorial(-1)) # 4 * 3 * 2 * 1 = 24
#
# def fun(a):
#     if a > 30:
#         return 3
#     else:
#         return a + fun(a + 3)
#
#
# print(fun(25))

# 4.6.1 Sequence types and mutability
# How to use a tuple
# my_tuple = (1, 10, 100, 1000)
#
# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])
#
# for elem in my_tuple:
#     print(elem)
#
# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3
#
# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

# var = 123
#
# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)
#
# t1, t2, t3 = t2, t3, t1
#
# print(t1, t2, t3)
# print(t1 + t2)
# print(t1, t2, t3)
# print(t2 * t1[0])
# print(t1, t2, t3)

# How to make a dictionary
# dictionary = {
#                 "horse": "cheval"             ,
#                 "cat": "chat"
#                 ,                "dog": "chien"
#              }
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310, 22657854310:'Suzy' }
# empty_dictionary = {}
#
# print(len(dictionary))
# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)
# print(dictionary['cat'])
# print(phone_numbers["Suzy"])
# print(phone_numbers[22657854310])
#
# words = ['cat', 'lion', 'horse']
#
# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")


# 4.6.4 Dictionary methods and functions
# dictionary = {
#     "horse": "cheval"             ,
#     "cat": "chat"
#     ,                "dog": "chien"
# }
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310, 22657854310:'Suzy' }
# empty_dictionary = {}
#
# # The keys() method
# # for key in dictionary.keys():
# #     print(key, "->", dictionary[key])
#
# # The items() method
# # The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair.
# for english, french in dictionary.items():
#     print(english, "->", french)
#
# # Modifying and adding values
# dictionary['cat'] = 'minou'
# print(dictionary)
#
# for key in sorted(dictionary.keys()):
#     print(key)
#
# # The values() method
# # As the dictionary is not able to automatically find a key for a given value, the role of this method is rather limited.
# for french in dictionary.values():
#     print(french)
#
# # Adding a new key
# dictionary['swan'] = 'cygne'
# print(dictionary)
#
# # You can also insert an item to a dictionary by using the update() method, e.g.:
# dictionary.update({"duck": "canard"})
# print(dictionary)
#
# # Removing a key
# # This is done with the del instruction.
# del dictionary['dog']
# # To remove the last item in a dictionary, you can use the popitem() method:
# dictionary.popitem()
# #sorted(dictionary.keys().popitem()) #does not sort and pop for some reason. still just pops last item of unsorted dictionary. might be because the sorted needs to work on the keys or values and not the dict as a whole
# print(dictionary)

# 4.6.5 Tuples and dictionaries can work together
# school_class = {}
#
# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
#
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
#
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     print(school_class[name])
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)
#     print(school_class)

# 4.6.6 SECTION SUMMARY
# # 1. Tuples are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists. They are written in round brackets:
# my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
# print(my_tuple)
#
# my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
# print(my_list)
#
# one_elem_tuple_1 = ("one",)    # Brackets and a comma.
# one_elem_tuple_2 = "one",       # No brackets, just a comma.
# one_elem_tuple_3 = ("one")    # Brackets and no comma will be treated as assigning a variable of the given type, not a tuple
# print(type(one_elem_tuple_1))
# print(type(one_elem_tuple_2))
# print(type(one_elem_tuple_3))

# 5. Tuples are immutable, which means you cannot change their elements (you cannot append tuples, or modify, or remove tuple elements). The following snippet will cause an exception:
# my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
# my_tuple += "e-guitar", # this allows you to "append" a tuple to an existing tuple. fails without the comma
# print(my_tuple)
# my_tuple[2] = "guitar"    # The TypeError exception will be raised.

# # 6. You can loop through a tuple elements (Example 1), check if a specific element is (not)present in a tuple (Example 2), use the len() function to check how many elements there are in a tuple (Example 3), or even join/multiply tuples (Example 4):
# # Example 1
# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)
#
# # Example 2
# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)
#
# # Example 3
# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)
# # Example 4
# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2
#
# print(tuple_4)
# print(tuple_5)

# # 4.6.7 SECTION QUIZ
# # Question 2: What is the output of the following snippet?
# tup = 1, 2, 3
# a, b, c = tup
# print(type(tup))
# print(a * b * c)

# # Question 3: Complete the code to correctly use the count() method to find the number of duplicates of 2 in the following tuple.
# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)
# print(duplicates)    # outputs: 4

# Question 4: Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# #my solution:
# for item in (d1, d2):
#     for key in item:
#         d3[key] = item[key]
#
# print(d3)

# # Course solution:
# for item in (d1, d2):
#     d3.update(item)
#
# print(d3)

# # Question 5: Write a program that will convert the my_list list to a tuple.
# my_list = ["car", "Ford", "flower", "Tulip"]
# # # mine
# # t = my_list[0], my_list[1], my_list[2], my_list[3]
# # print(t)
# # course answer
# t = tuple(my_list)
# print(t)

# Question 6: Write a program that will convert the colors tuple to a dictionary.
# colors = (("green", "#008000"), ("blue", "#0000FF"))
# # me
# # print(colors[0])
# # for i in colors[0]:
# #     print(i)
# colors_dictionary={}
# colors_dictionary[colors[0][0]] = colors[0][1]
# colors_dictionary[colors[1][0]] = colors[1][1]
# # colors_dictionary.update(colors[0])
# # colors_dictionary.update(colors[1])
#
# print(colors_dictionary)

# # them
# colors_dictionary = dict(colors)
# print(colors_dictionary)


colors = {
    "white": (255, 255, 255),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0)
}

for col, rgb in colors.items():
    print(col, ":", rgb)

print(colors)
