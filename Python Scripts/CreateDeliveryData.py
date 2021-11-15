from random import randrange





with open("input32.txt", "r") as f:
    nodeFlag = 0
    weightFlag = 0
    locationsArray = []
    weightArray = []
    for line in f:
        if "DIMENSION" in line:
            lineList = []
            for word in line.split():
                lineList.append(word)
            n = int(lineList[2]) #the third string is the demention
        elif "NODE_COORD_SECTION" in line:
            nodeFlag = 1
            continue
        elif "DEMAND_SECTION" in line:
            weightFlag = 1
            nodeFlag = 0
            continue
        elif "DEPOT_SECTION" in line:
            break
        elif nodeFlag == 1 :
            lineList = []
            for word in line.split():
                lineList.append(word)
            if lineList[0] != "1":
                x = lineList[1]
                y = lineList[2]
                locationsArray.append((x,y))#add the cordinats to the array
        elif weightFlag == 1 :
            lineList = []
            for word in line.split():
                lineList.append(word)
            if lineList[0] != "1":
                w = lineList[1]
                weightArray.append(w)#add the weight to the array

    retval = ""
    retval = retval + "[\n"
    for i in range (1,n):
        retval = retval + "\t{\n"
        retval = retval + "\t\t\"id\": " + str(i) + ",\n"
        retval = retval + "\t\t\"name\": " "\"yuval\"" + ",\n"
        retval = retval + "\t\t\"value\": " + str(randrange(5,20)) + ",\n"
        #retval = retval + "\t\t\"value\": " + str(1) + ",\n"
        retval = retval + "\t\t\"weight\": " + str(weightArray[i-1]) + ",\n"
        retval = retval + "\t\t\"locationX\": " + str(locationsArray[i-1][0]) + ",\n"
        retval = retval + "\t\t\"locationY\": " + str(locationsArray[i-1][1]) + "\n"
        if i != n-1:
            retval = retval + "\t},\n"
        else:
            retval = retval + "\t}\n"
            retval = retval + "]"
    file = open("Catalog.json", "w")
    file.write(retval)
    file.close()
