import os
from HelperFunctions import *

#item groups are basicly filters and files visible in the solution
#This function adds them to the project configuration specified in 
def FixItemGroups(GeneratedProject, FixedProject):
    indexOfItemGroups = GeneratedProject.find("<ItemGroup>")
    itemGroups = generatedProjectData[indexOfItemGroups:len(generatedProjectData)]
    return FixedProject + itemGroups

#Set the project name to the same name used in the main.sharpmake.cs
def FixProjectName(Name, FixedProject):
    tag = "ProjectName"

    entryTag = "<"+tag+">"
    startIndex = FixedProject.find(entryTag) + len(entryTag)
    endIndex = FixedProject.find("</"+tag+">")

    text = DeleteText(startIndex, endIndex, FixedProject)
    text = InsertText(Name, startIndex, text)
    return text

    

MainSharpmakePath = os.getcwd()+ "\\main.sharpmake.cs"
ProjectName = FindProjectNameInSharpmake(MainSharpmakePath)

GemeratedProjectFilePath = os.getcwd() + "\\..\\"+ProjectName+".vcxproj"
ProjectFilePathWithGoodConfiguration = os.getcwd()+ "\\ProjectContent.txt"

manualyCreatedProjectData = ReadFromFile(ProjectFilePathWithGoodConfiguration)
generatedProjectData = ReadFromFile(GemeratedProjectFilePath)

manualyCreatedProjectData = FixItemGroups(generatedProjectData, manualyCreatedProjectData)
manualyCreatedProjectData = FixProjectName(ProjectName, manualyCreatedProjectData)

WriteToFile(GemeratedProjectFilePath, manualyCreatedProjectData)
