with open('C:\Computer Science\AdventofCode22\Day4\input.txt') as f:

    newlines = f.readlines()

    # list of repeated elements per three rucksacks
    badges = []
    priorities = 0

    # removing new line characters
    lines = []
    for line in newlines:
        lines.append(line.replace("\n", ""))

    count = 0

    for line in lines:
        # retrieving the two ranges
        commaSplit = line.split(",")
        rangeOne = commaSplit[0]
        rangeTwo = commaSplit[1]

        #
        rangeOneSplit = rangeOne.split("-")
        rangeTwoSplit = rangeTwo.split("-")

        # retrieving upper and lower bounds of range One
        rangeOneLower = int(rangeOneSplit[0])
        rangeOneUpper = int(rangeOneSplit[1])

        # retrieving upper and lower bounds of range Two
        rangeTwoLower = int(rangeTwoSplit[0])
        rangeTwoUpper = int(rangeTwoSplit[1])

        # checking if ranges fully contain each other
        if (rangeOneLower <= rangeTwoLower and rangeOneUpper >= rangeTwoUpper) or (rangeOneLower >= rangeTwoLower and rangeOneUpper <= rangeTwoUpper):
            count += 1

    # outputting final answer
    print(count)
