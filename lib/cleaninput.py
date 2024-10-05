def getfileInputLinesAsList(fileName):
    with open(fileName) as handle:
        text = handle.readlines()

    textNew = []
    for line in text:
        textNew.append(line.replace('\n','').replace('\r',''))

    return textNew