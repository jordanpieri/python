'''
def find_anagrams(word, candidates):
    pass
    check = []
    for x in word:
        check.append(x)
        print("line 6. check: ", check, ". x: ", x, sep="")
        r = range(len(candidates))
        for i in range(r):
            print("line 8. candidates: ", candidates, ". i: ", i, "candidates[i]: ", candidates[i], sep="")
            if check in candidates[i]:
                return candidates[i]
'''


def find_anagrams(word, candidates):
    pass
    check = []
    match = 0
    solution = []
    for x in word:
        check.append(x)
        # print("line 6. check: ", check, ". x: ", x, sep="")
    for i in range(len(candidates)):
        # print("line 9. candidates: ", candidates, ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
        print()
        print("Checking candidate number ", i + 1, ", '", candidates[i], "' of list: ", candidates, sep="")
        print("Is '", word, "' the same as '", candidates[i], "'?", sep="")
        if word.lower() == candidates[i].lower():
            print("The word '", word, "' is not an anagram of '", candidates[i],
                  "' because they are the same word.", sep="")
                    # print("line 11. x: ", x, ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
                    print("Let's see if letter number ", x + 1, " (", check[x], ") is in ", candidates[i], ":", sep="")
            if check[x].lower() in candidates[i].lower():
                # print("line 13. check[x]: ", check[x], ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
                match += 1
                print("Yes, '", check[x], "' is in '", candidates[i], "', so increase matches to:", match, "/",
                      len(candidates[i]), sep="")
                # print("match: ",match,sep="")
            if match == len(candidates[i]):
                # print("returning",candidates[i])
                solution.append(candidates[i])
                print("We have counted ", match, " matches out of ", len(candidates[i]),
                      ". So let's add this word: ", candidates[i], " to our solution.", solution, sep="")
                #print()
                break
                # return candidates[i]
                # if match < len(candidates[i]):
                # print("Counting ",match, "/", len(candidates[i]), sep="")
                if match > len(candidates[i]):
                    # print("else line 20. check[x]: ", check[x], ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
                    print("Match count is ", match, " out of ", len(candidates[i]), ". Unexpected ending", sep="")
                # if check in candidates[i]:
                # return candidates[i]
                if x + 1 == len(candidates[i]):
                    print("We have reached the end of counting candidate number ", i + 1, ", ", candidates[i], ". The count is ", x + 1, "/",
                          len(candidates[i]), sep="")
                    # if match == len(candidates[i]):
                    #    print("returning", candidates[i])
                    #    return candidates[i]
                    if match < len(candidates[i]):
                        print("Not enough matches (", match, "/", len(candidates[i]), "). Continue to next.", sep="")
                        continue
                    x += 1
                    # print("x is now '", x, "'.", sep="")
                # print("line z. check letters ", check, " in current (", i + 1, ") candidate ", (candidates[i]), sep="")
                # print("1. Done processing candidate ", i + 1, ", ", candidates[i], sep="")
            else:
                print("The word '", word, "' is not an anagram of '", candidates[i],
                      "' because they are not the same length.", sep="")
            print("Done processing candidate ", i + 1, ", ", candidates[i], sep="")
        i += 1
        # print("i is now '", i, "'.", sep="")
        match = 0
        print()
    print("Solution: ", solution, sep="")
    return solution
