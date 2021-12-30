import configparser
import time
import chevron
import tkinter
from tkinter import *
from tkinter.colorchooser import askcolor

# Read config file
config = configparser.ConfigParser()
config.read("config.ini")

settings = config["Settings"]
clearSetting = int(settings["clearSetting"])
loopFormatting = int(settings["loopFormatting"])
printToConsole = bool(int(settings["printToConsole"]))
namingScheme = int(settings["namingScheme"])
recolourHelperMode = int(settings["recolourHelperMode"])

output1 = config["Output Files"]["output1"]

# UI stuffs
dummyGUIThing = Tk()
dummyGUIThing.title("Ignore this window")
dummyGUIThing.geometry("1x1")

# Various dictionaries
templateDictionary = {
    0: config["Templates"]["colourTemplate"],
    1: config["Templates"]["recolourHelperTemplate"]
}

colourParameterDictionary = {
    0 : "rgb",
    1 : "xyz"
}

optionStrings = {
    1 : "color",
    2 : "emissiveColor",
    3 : "initialColor",
    4 : "Custom name"
}

modeStrings = {
    0 : "",
    1 : "\ncolourFormatter is running in recolourHelper compatibility mode"
}

# Brings up the colour picker UI for the user to pick a colour, then returns it as an RGB tuple
def getColour (
    ):

    colours = askcolor(title = "Pick a colour, any colour ...")
    return tuple(colours[0]) # 0 is RBG, 1 is hex

# Takes the chosen field name and colour, and formats it
def formatColour(
    fieldName,
    rgbColour
    ):
    
    parameterName = colourParameterDictionary[namingScheme]

    args = {
        'fieldName' : fieldName,
        'r' : rgbColour[0],
        'g' : rgbColour[1],
        'b' : rgbColour[2],
        'floatR' : rgbColour[0]/255,
        'floatG' : rgbColour[1]/255,
        'floatB' : rgbColour[2]/255,
        'parameterR' : parameterName[0],
        'parameterG' : parameterName[1],
        'parameterB' : parameterName[2]
    }

    # Open template and pass through args
    with open(templateDictionary[recolourHelperMode], 'r') as entityTemplate:
        generatedEntity = chevron.render(entityTemplate, args)
        if printToConsole: # Print formatted colour to console if the option is enabled in the config
            print("\n" + generatedEntity)

    # Write formatted colour to file
    writeStuffToFile(generatedEntity, output1)

# Write the given input to the given output file
def writeStuffToFile(
    inputItem,
    outputFile
    ):

    # Open output txt and write spawn targets to file
    with open(outputFile, 'a') as output_File:
        output_File.write("\n" + inputItem)

# Tells user to pick the colour field name, then calls the other functions that handle actual colour picking and formatting
def colourPicker(
    ):
    
    fieldName = str("")

    if recolourHelperMode == 0:
        print("\nSet the name for colour field:")
        for i in range (1, len(optionStrings) + 1):
            print(str(i) + ". " + optionStrings[i])

        colourOption = int(input())
        while True:
            if colourOption > len(optionStrings) or colourOption < 1:
                colourOption = int(input("Invalid option, try again: "))
            else:
                break

        if colourOption == len(optionStrings):
            fieldName = str(input("Enter custom field name: "))
        else:
            fieldName = optionStrings[colourOption]

    rgbColour = getColour()
    formatColour(fieldName, rgbColour)

# Clears the output file
def clearOutput(
    ):

    with open(output1, 'w') as outFile:
        outFile.write("")
        outFile.close()

# "Main"
def mainBody(
    ):

    titleString = "colourFormatter v0.1 by elizabethany"
    borderString = ""
    for i in range (0, len(titleString)):
        borderString += "="
    
    print(borderString)
    print(titleString)
    print(borderString)
    time.sleep(0.1)
    print(modeStrings[recolourHelperMode])
    time.sleep(0.1)

    if clearSetting == 0:
        # Ask user if they want to clear the output file, then clear it if the option was selected
        manualClear = input("\nClear the output files from previous sessions? (Y/N): ");
        if manualClear == 'y' or manualClear == 'Y':
            clearOutput()
    elif clearSetting == 2:
        clearOutput()
    
    while True:
        dummyGUIThing.withdraw()
        colourPicker()
        if loopFormatting == 0:
            break
        time.sleep(0.2)

mainBody()