from ..Tools.CaseHandler import toCodeCamelCase

def getSanitiZerFileName(catName):
    return toCodeCamelCase(catName + "Sanitizer.ts")

def getSanitiZerMiddlewareName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Sanitizer")

