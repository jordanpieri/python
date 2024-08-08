beatles = []
print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
beatles.append("Ringo Starr")

print("Step2:", beatles)
list_length = 2
for x in range(list_length):
    mem = input("Then who? (Add Stu Sutcliffe & Pete Best: ")
    beatles.append(mem)

print("Step 3:", beatles)
#print("beatle 0:", beatles[0])
#print("beatle 1:", beatles[1])
#print("beatle 2:", beatles[2])
#print("beatle 3:", beatles[3])
#print("beatle 4:", beatles[4])
del beatles[5]
del beatles[4]

print("Step 4:", beatles)

#print("Step 5:", beatles)

print("The Fab", len(beatles))