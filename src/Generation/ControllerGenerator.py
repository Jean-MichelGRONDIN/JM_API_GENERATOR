from ..Tools.CaseHandler import toCodeCamelCase

def getControllerFileName(catName):
    return toCodeCamelCase(catName + ".controller.ts")


def getControllerMiddlewareName(actionName):
    return toCodeCamelCase(actionName)

