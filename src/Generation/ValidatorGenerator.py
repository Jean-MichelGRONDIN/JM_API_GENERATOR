from ..Tools.JsonHandler import JsonHandler
from ..Tools.CaseHandler import toCodeCamelCase

def getValidatorFileName(catName):
    return toCodeCamelCase(catName + "Validator.ts")

def getValidatorMiddlewareName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Validator")

def hasValidator(json):
    data = json.access('data')
    for elem in data:
        elemJson = JsonHandler(elem)
        if elemJson.access('validator.has'):
            return True
    return False
