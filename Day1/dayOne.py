
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
    sums.sort()
    print(sums)

    #the answer would be the element at index -1 in the list [highest calories]