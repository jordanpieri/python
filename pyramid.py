#blocks = int(input("Enter the number of blocks: "))
block = [6,20,1000,2]
for blocks in block:
    height = 0
    while True:
        remainder = blocks - height
        if remainder > height:
            blocks -= height
            height += 1
        else:
            print("remainder: ",remainder,". blocks: ",blocks," . height: ",height,sep="")
            print("insufficient blocks, stopping.")
            break
    print("The height of the pyramid:", height)



