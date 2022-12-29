
with open('C:\Computer Science\AdventofCode22\Day3\input.txt') as f:

    lines = f.readlines()
    
    #list of repeated elements 
    wrongTypes = []
    priorities = 0

    for line in lines:

        #breaking rucksack into to compartments
        compLength = len(line)
        compOne = line[0:(compLength//2)]
        compTwo = line[compLength//2:compLength]


        #using lists for both the compartments
        compOneList = []
        compTwoList = []

        for i in range(len(compOne)):
            compOneList.append(compOne[i])
            compTwoList.append(compTwo[i])

        #converting lists to sets for intersection
        compOneSet = set(compOneList)
        compTwoSet = set(compTwoList)
        interSet = set.intersection(compOneSet, compTwoSet)
        for element in interSet:
            wrongTypes.append(element)


    for type in wrongTypes:
        if type.isupper():
            #uppercase
            priorities += ord(type) - 38

        else:
            #lowercase
            priorities += ord(type) - 96
     
     #outputting total priotity
    print(priorities)
                