
with open('C:\Computer Science\AdventofCode22\Day1\input.txt') as f:
    lines = f.readlines()

    maxNum = 0
    sum = 0

    for line in lines:
        if line == '\n':
            #print("hi")
            if sum > maxNum:
                maxNum = sum
            sum = 0
        else:
            print(line)
            sum += int(line[0:len(line)-2])
    
    print(maxNum)