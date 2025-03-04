# # 8/8/2024:
# '''
# def find_anagrams(word, candidates):
#     pass
#     check = []
#     for x in word:
#         check.append(x)
#         print("line 6. check: ", check, ". x: ", x, sep="")
#         r = range(len(candidates))
#         for i in range(r):
#             print("line 8. candidates: ", candidates, ". i: ", i, "candidates[i]: ", candidates[i], sep="")
#             if check in candidates[i]:
#                 return candidates[i]
# '''
#
#
# def find_anagrams(word, candidates):
#     pass
#     check = []
#     match = 0
#     solution = []
#     for x in word:
#         check.append(x)
#         # print("line 6. check: ", check, ". x: ", x, sep="")
#     for i in range(len(candidates)):
#         # print("line 9. candidates: ", candidates, ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
#         print()
#         print("Checking candidate number ", i + 1, ", '", candidates[i], "' of list: ", candidates, sep="")
#         print("Is '", word, "' the same as '", candidates[i], "'?", sep="")
#         if word.lower() == candidates[i].lower():
#             print("The word '", word, "' is not an anagram of '", candidates[i],
#                   "' because they are the same word.", sep="")
#                     # print("line 11. x: ", x, ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
#                     print("Let's see if letter number ", x + 1, " (", check[x], ") is in ", candidates[i], ":", sep="")
#             if check[x].lower() in candidates[i].lower():
#                 # print("line 13. check[x]: ", check[x], ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
#                 match += 1
#                 print("Yes, '", check[x], "' is in '", candidates[i], "', so increase matches to:", match, "/",
#                       len(candidates[i]), sep="")
#                 # print("match: ",match,sep="")
#             if match == len(candidates[i]):
#                 # print("returning",candidates[i])
#                 solution.append(candidates[i])
#                 print("We have counted ", match, " matches out of ", len(candidates[i]),
#                       ". So let's add this word: ", candidates[i], " to our solution.", solution, sep="")
#                 #print()
#                 break
#                 # return candidates[i]
#                 # if match < len(candidates[i]):
#                 # print("Counting ",match, "/", len(candidates[i]), sep="")
#                 if match > len(candidates[i]):
#                     # print("else line 20. check[x]: ", check[x], ". i: ", i, ". candidates[i]: ", candidates[i], sep="")
#                     print("Match count is ", match, " out of ", len(candidates[i]), ". Unexpected ending", sep="")
#                 # if check in candidates[i]:
#                 # return candidates[i]
#                 if x + 1 == len(candidates[i]):
#                     print("We have reached the end of counting candidate number ", i + 1, ", ", candidates[i], ". The count is ", x + 1, "/",
#                           len(candidates[i]), sep="")
#                     # if match == len(candidates[i]):
#                     #    print("returning", candidates[i])
#                     #    return candidates[i]
#                     if match < len(candidates[i]):
#                         print("Not enough matches (", match, "/", len(candidates[i]), "). Continue to next.", sep="")
#                         continue
#                     x += 1
#                     # print("x is now '", x, "'.", sep="")
#                 # print("line z. check letters ", check, " in current (", i + 1, ") candidate ", (candidates[i]), sep="")
#                 # print("1. Done processing candidate ", i + 1, ", ", candidates[i], sep="")
#             else:
#                 print("The word '", word, "' is not an anagram of '", candidates[i],
#                       "' because they are not the same length.", sep="")
#             print("Done processing candidate ", i + 1, ", ", candidates[i], sep="")
#         i += 1
#         # print("i is now '", i, "'.", sep="")
#         match = 0
#         print()
#     print("Solution: ", solution, sep="")
#     return solution

# 2/10/2025:
def find_anagrams(word, candidates):
    result = []
    if len(word) > 0:
        a = sort_word(word.lower())
        #print("a:",a, word)
        for i in range(len(candidates)):
            if word.lower() == candidates[i].lower():
                #print("Same word:",word,"==", candidates[i], i)
                #return '' # prevents subsequent candidates from processing
                # break '' # prevents subsequent candidates from processing
                continue
            b = sort_word(candidates[i].lower())
            #print("b:",b, i, candidates[i])
            if a == b:
                result.append(candidates[i])
            #else:
            #    print("no match:", word, candidates[i])
    return result


def sort_word(word):
    l = []
    #word.lower()
    for i in word:
        l.append(i)
    #l.lower()
    l.sort()
    return l

# candidates = ["stream", "pigeon", "maters"]
# # expected = ["stream", "maters"]
# print(find_anagrams("master", candidates))
# #candidates = ["cashregister", "Carthorse", "radishes", "Orchestra"]
# #print(find_anagrams("Orchestra", candidates))
# candidates = ["BANANA", "Banana", "banana"]
# print(find_anagrams("BANANA", candidates))
# candidates = ["Listen", "Silent", "LISTEN"]
# print(find_anagrams("Silent", candidates))
#




import unittest

from anagram import find_anagrams


class AnagramTest(unittest.TestCase):
    def test_no_matches(self):
        candidates = ["hello", "world", "zombies", "pants"]
        expected = []
        self.assertCountEqual(find_anagrams("diaper", candidates), expected)

    def test_detects_two_anagrams(self):
        candidates = ["stream", "pigeon", "maters"]
        expected = ["stream", "maters"]
        self.assertCountEqual(find_anagrams("master", candidates), expected)

    def test_does_not_detect_anagram_subsets(self):
        candidates = ["dog", "goody"]
        expected = []
        self.assertCountEqual(find_anagrams("good", candidates), expected)

    def test_detects_anagram(self):
        candidates = ["enlists", "google", "inlets", "banana"]
        expected = ["inlets"]
        self.assertCountEqual(find_anagrams("listen", candidates), expected)

    def test_detects_three_anagrams(self):
        candidates = ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
        expected = ["gallery", "regally", "largely"]
        self.assertCountEqual(find_anagrams("allergy", candidates), expected)

    def test_detects_multiple_anagrams_with_different_case(self):
        candidates = ["Eons", "ONES"]
        expected = ["Eons", "ONES"]
        self.assertCountEqual(find_anagrams("nose", candidates), expected)

    def test_does_not_detect_non_anagrams_with_identical_checksum(self):
        candidates = ["last"]
        expected = []
        self.assertCountEqual(find_anagrams("mass", candidates), expected)

    def test_detects_anagrams_case_insensitively(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        self.assertCountEqual(find_anagrams("Orchestra", candidates), expected)

    def test_detects_anagrams_using_case_insensitive_subject(self):
        candidates = ["cashregister", "carthorse", "radishes"]
        expected = ["carthorse"]
        self.assertCountEqual(find_anagrams("Orchestra", candidates), expected)

    def test_detects_anagrams_using_case_insensitive_possible_matches(self):
        candidates = ["cashregister", "Carthorse", "radishes"]
        expected = ["Carthorse"]
        self.assertCountEqual(find_anagrams("orchestra", candidates), expected)

    def test_does_not_detect_an_anagram_if_the_original_word_is_repeated(self):
        candidates = ["go Go GO"]
        expected = []
        self.assertCountEqual(find_anagrams("go", candidates), expected)

    def test_anagrams_must_use_all_letters_exactly_once(self):
        candidates = ["patter"]
        expected = []
        self.assertCountEqual(find_anagrams("tapper", candidates), expected)

    def test_words_are_not_anagrams_of_themselves_case_insensitive(self):
        candidates = ["BANANA", "Banana", "banana"]
        expected = []
        self.assertCountEqual(find_anagrams("BANANA", candidates), expected)

    def test_words_other_than_themselves_can_be_anagrams(self):
        candidates = ["Listen", "Silent", "LISTEN"]
        expected = ["Silent"]
        self.assertCountEqual(find_anagrams("LISTEN", candidates), expected)


if __name__ == "__main__":
    unittest.main()
