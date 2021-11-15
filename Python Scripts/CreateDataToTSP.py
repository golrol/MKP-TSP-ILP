import json
import numpy as np
import sys
import math

'''
functio that get file name as argument and create 
array of array for the next function to work with.
'''
def creatArrys(fileName):

    i=0
    retValue=[]

    with open(fileName,"r") as f:
        for line in f:

            if "Capacity" in line:#init the idList evry time "Capacity" is found - new Vehicle
                i=i+1
                idList = []

            elif "Item" in line:
                lineList = []
                for word in line.split():
                    lineList.append(word) #index number 3 is "id" of the packge.
                idList.append(int(lineList[3]))


            elif "Total" in line:
                retValue.append(idList)
    return retValue


    

'''
functio that get array of array and create
an matrix of distances for the items to deliver
return: matrix
'''
def PointToMatrix(array):#array is array of arrays#
    f = open("Catalog.json")
    catalog = json.load(f)
    pointsArray = []
    VehicleNumber=0

    for currentArray in array:
        VehicleNumber = VehicleNumber+1
        pointsArray.append((86, 76))#Base location
        for i in currentArray:
            for item in catalog:
                if item["id"] == i:
                    pointsArray.append((item["locationX"], item["locationY"]))

        matrix = np.zeros((len(pointsArray), len(pointsArray)), dtype=np.int32)

        for i in range(len(pointsArray)):
            for j in range(len(pointsArray)):
                if i == j:
                    matrix[i][j] = 99999
                else:
                    matrix[i][j] = np.round(math.dist(pointsArray[i], pointsArray[j]))

        # np.set_printoptions(suppress=True, precision=3)
        # print(repr(matrix))#make the matrix into string
        pointsArray = []
        creatTSPInput(matrix,VehicleNumber,currentArray)
    f.close()
    return matrix


def creatTSPInput(matrix,index,currentArray):
    newFileName = "myTSP\TSPinput" + str(index) + ".dat"

    f = open(newFileName, "w")
    size = len(matrix)  # get the size of teh matrix

    # format for the TSP input.
    st = "Vehicle=" + str(index) + ";\n"
    currentArray.insert(0, 0)
    st = st + "n=" + str(size) + ";\n"
    st = st + "IndexArray=" + str(currentArray) + ";\n"
    st = st + "dist = [\n"
    for i in range(size):
        st = st + "["
        for j in range(size):
            val = matrix[i][j]
            if j < size - 1:
                st = st + str(val) + ","
            else:
                if i != size - 1:
                    st = st + str(val) + "],\n"
                else:
                    st = st + str(val) + "]"
    st = st + "\n];"
    f.write(st)
    f.close()
    # print (st)


if __name__ == '__main__':
    a = creatArrys("knapSackOutput.txt")#creat the array to create the matrix
    m = PointToMatrix(a)#get the matrix out of teh array



    
