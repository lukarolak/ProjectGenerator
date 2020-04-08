def ReadFromFile(Path):
    openedFile = open(Path, "r")
    content = openedFile.read()
    openedFile.close()
    return content

def WriteToFile(Path, content):
    openedFile = open(Path, "w")
    openedFile.write(content)
    openedFile.close()

def InsertText(InsertText, Index, Content):
    text = Content[:Index] + InsertText + Content[Index:]
    return text

def DeleteText(StartIndex, EndIdex, Content):
    text = Content[:StartIndex] + Content[EndIdex:]
    return text

def FindProjectNameInSharpmake(path):
    mainSharpmake = ReadFromFile(path)
    tag = "Name = \""

    startIndex = mainSharpmake.find(tag) + len(tag)
    endIndex = mainSharpmake.find("\"",startIndex)

    projectName = mainSharpmake[startIndex:endIndex]
    return projectName