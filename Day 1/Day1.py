maxCals = 0
elfNumber = 0
elfCalCount = [0]
elfWithLargestPack = 0
with open('calories.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    calstr = line.strip('\0\n')
    if calstr.isnumeric():
        currCal = int(calstr)
        elfCalCount[elfNumber] = elfCalCount[elfNumber]+currCal # add the current calories to the count
    else:
        elfNumber += 1 # go to next elf's stash
        elfCalCount.append(0)
elfNumber = 0
for elfPack in elfCalCount:
    if elfPack > maxCals:
        maxCals = elfPack
        elfWithLargestPack = elfNumber
    elfNumber += 1
print("There are "+str(len(elfCalCount))+" elves in this merry band")
print("The most prepared elf is "+str(elfWithLargestPack)+" with "+str(maxCals)+" in his bag")

# Part B addition
elfCalCount.sort()
topElves = elfCalCount[-3:]
totalCals = 0
for elfPack in topElves:
    totalCals = totalCals + elfPack
print("The top three most prepared elfs have "+str(totalCals)+" calories between them")
