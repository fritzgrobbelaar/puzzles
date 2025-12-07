import os
def getfileInputLinesAsList(fileName):
    with open(os.getcwd() + '/' + fileName) as handle:
        text = handle.readlines()

    textNew = []
    for line in text:
        textNew.append(line.replace('\n','').replace('\r',''))

    return textNew


def convertRowsOfTextToRowsOfNumbers(rows):
    newRows = []
    for row in rows:
        rowNew = []
        rowPart = row.split()
        for value in rowPart:
            rowNew.append(int(value))
        newRows.append(rowNew)
    return newRows

def getRowsOfNumbersLists(fileName):
    rows = getfileInputLinesAsList(fileName)
    return convertRowsOfTextToRowsOfNumbers(rows)