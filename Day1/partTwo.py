
with open('C:\Computer Science\AdventofCode22\Day1\input.txt') as f:
    lines = f.readlines()

    sum = 0
    sums = []

    for line in lines:
        if line == '\n':
            #print("hi")
            sums.append(sum)
            sum = 0
        else:
            print(line)
            sum += int(line)
    sums.sort(reverse=True)
    topThree = sums[0] + sums[1] + sums[2]
    print(topThree)

    #the answer would be the first three elements of the reverse sorted list