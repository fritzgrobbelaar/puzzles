import os
def getfileInputLinesAsList(fileName):
    with open(os.getcwd() + '/' + fileName) as handle:
        text = handle.readlines()

    textNew = []
    for line in text:
        textNew.append(line.replace('\n','').replace('\r',''))

    return textNew