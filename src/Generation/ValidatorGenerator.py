from ..Tools.CaseHandler import toCodeCamelCase

def getValidatorFileName(catName):
    return toCodeCamelCase(catName + "Validator.ts")
