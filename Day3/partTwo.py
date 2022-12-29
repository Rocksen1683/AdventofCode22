
with open('C:\Computer Science\AdventofCode22\Day3\input.txt') as f:

    newlines = f.readlines()

    # list of repeated elements per three rucksacks
    badges = []
    priorities = 0

    # removing new line characters
    lines = []
    for line in newlines:
        lines.append(line.replace("\n", ""))

    for i in range(0, len(lines), 3):
        elfOne = lines[i]
        elfTwo = lines[i+1]
        elfThree = lines[i+2]

        elfOneList = []
        elfTwoList = []
        elfThreeList = []

        # adding elements to list
        for j in range(len(elfOne)):
            elfOneList.append(elfOne[j])
        for j in range(len(elfTwo)):
            elfTwoList.append(elfTwo[j])
        for j in range(len(elfThree)):
            elfThreeList.append(elfThree[j])

        # converting lists into set
        elfOneSet = set(elfOneList)
        elfTwoSet = set(elfTwoList)
        elfThreeSet = set(elfThreeList)

        # intersection of sets
        interSet = set.intersection(elfOneSet, elfTwoSet, elfThreeSet)

        for element in interSet:
            badges.append(element)

    for type in badges:
        if type.isupper():
            # uppercase
            priorities += ord(type) - 38

        else:
            # lowercase
            priorities += ord(type) - 96

     # outputting total priotity
    print(priorities)
