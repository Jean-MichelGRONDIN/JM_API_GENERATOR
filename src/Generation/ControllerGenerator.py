from ..Tools.CaseHandler import toCodeCamelCase

def getControllerFileName(catName):
    return toCodeCamelCase(catName + ".controller.ts")
