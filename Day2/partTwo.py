
with open('C:\Computer Science\AdventofCode22\Day2\input.txt') as f:
    lines = f.readlines()
    
    #making a symbol map based on rules
    pointMap = {"Rock":1,"Paper":2,"Scissors":3}
    decisionMap = {"X":"Lose","Y":"Draw","Z":"Win"}
    symbolMap = {"A":"Rock","B":"Paper","C":"Scissors"}
    winMap = {"Rock":"Paper","Paper":"Scissors","Scissors":"Rock"}
    drawMap = {"Rock":"Rock","Paper":"Paper","Scissors":"Scissors"}
    loseMap = {"Rock":"Scissors","Paper":"Rock","Scissors":"Paper"}
    """
    Rock - 1 
    Paper - 2 
    Scissors - 3

    Win - 6
    Draw - 3
    Lose - 0
    """

    totalPoints = 0
    count = 0

    for line in lines:
        splitLine = line.split(" ")
        if splitLine[1] == "X\n":
            #lose
            totalPoints += pointMap[loseMap[symbolMap[splitLine[0]]]]
        elif splitLine[1] == "Y\n":
            #draw
            totalPoints += 3
            totalPoints += pointMap[drawMap[symbolMap[splitLine[0]]]]
        elif splitLine[1] == "Z\n":
            #win
            totalPoints += 6
            totalPoints += pointMap[winMap[symbolMap[splitLine[0]]]]
        elif splitLine[1] == "Z":
            #win
            totalPoints += 6
            totalPoints += pointMap[winMap[symbolMap[splitLine[0]]]]
        count += 1
    print(totalPoints)
    print(count)
    #total points is the final answer

    