from ..Tools.CaseHandler import toCodeCamelCase

def getValidatorFileName(catName):
    return toCodeCamelCase(catName + "Validator.ts")

def getValidatorMiddlewareName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Validator")
