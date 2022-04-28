"""
Work out the first teon digits of the following 100 50 digit numbers (in ProjEuler_Problem-13_DataArray.csv)
"""


import timeit                           #used to test algorithmic efficiency
import csv

dataGrid = []                           #global storage for data set
digBound = 11                           #how many digs are we checking

#function for taking raw data (in csv format) and building into global "dataGrid" multidimensional list
def dataImport():                                                   
    with open("ProjEuler_Problem-13_DataArray.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)        # sets up reader
        for row in reader:                                          # each row is a list
            dataGrid.append(row)                                    #csvfile readline might be a better choice!

#Kludgy method with 0 finesse
def method0():
    dataImport()
    digSum = 0
    gridSize = len(dataGrid)

    for i in range(0, gridSize):
        digSum = digSum+int(dataGrid[i][0])

    print(str(digSum)[0:(digBound-1)])

#treat as an array & only sum needed digits; uses more processor iterations, but less large int calculations
def method1():
    dataImport()
    digSum = []

    gridSize = len(dataGrid)
    for i in range(0,digBound):
        digSum.append(0)

    for i in range(0,gridSize):             #technically incomplete; needs some logic for a rollover case (999 on last dig) to extend down
        tmpStr = str(dataGrid[i][0])
        for j in range(0,digBound):
            relDig = tmpStr[j]
            digSum[j] += int(relDig)

    fullSum = 0
    for i in range(0,digBound):
        fullSum = fullSum + (digSum[digBound-i-1] * (pow(10,i)))
    
    print(str(fullSum)[0:(digBound-1)])

method0()
