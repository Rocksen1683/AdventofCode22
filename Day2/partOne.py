
with open('C:\Computer Science\AdventofCode22\Day2\input.txt') as f:
    lines = f.readlines()
    
    #making a symbol map based on rules
    symbolMap = {"A":"Rock","B":"Paper","C":"Scissors",
                 "X":"Rock","Y":"Paper","Z":"Scissors"}
    """
    Rock - 1 
    Paper - 2 
    Scissors - 3

    Win - 6
    Draw - 3
    Lose - 0
    """

    #made point map based on rules
    pointMap = {"A X\n" :4, "A Y\n":8, "A Z\n":3,
                "B X\n" :1, "B Y\n":5, "B Z\n":9,
                "C X\n" :7, "C Y\n":2, "C Z\n":6,
                "A X" :4, "A Y":8, "A Z":3,
                "B X" :1, "B Y":5, "B Z":9,
                "C X" :7, "C Y":2, "C Z":6}

    totalPoints = 0
    count = 0

    for line in lines:
        totalPoints += pointMap[line]
        count += 1
    print(totalPoints)
    print(count)
    #total points is the final answer

    