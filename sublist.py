def sublist(list_one, list_two):
    pass
    match = 0
    if list_one:
        print("line 25. list_one if passed")
        print(list_one, list_two)
    else:
        print("line 28. what the frick, list_one is False: ", list_one, list_two)
        print("list_one is a(n) ", type(list_one), ". list_two is a(n) ", type(list_two))
        #return
    if list_one is None:
        print("line 31. list_one is None")
        print("line 32. ", list_one, list_two)
    else:
        print("line 34. what the frick, list_one is not None??")
    print("line 35. ", list_one, list_two)

    if len(list_one) == 1:
        print("line 38. len is 1, UNEQUAL")
        return UNEQUAL
    for x in range(len(list_one)):
        print("line 41. list_one[",x,"]", "in list_two(",list_two)
        if list_one[x] in list_two:
            match += 1
            print("line 44. match: ",match)
    if match > 2:
        print("if match > 2: ")
        if len(list_one) > len(list_two):
            print("SUPERLIST")
            return SUPERLIST
        if len(list_one) < len(list_two):
            print("SUBLIST")
            return SUBLIST
        if len(list_one) == len(list_two):
            print("EQUAL")
            return EQUAL
    else:
        print("line 57. else UNEQUAL")
        return UNEQUAL