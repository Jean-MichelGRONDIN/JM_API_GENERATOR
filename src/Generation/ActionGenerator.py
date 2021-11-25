from ..Tools.CaseHandler import toCodeCamelCase
from .ModelGenerator import getModelFileNameFromCatName

def getActionFileName(catName):
    return toCodeCamelCase(catName + "Action.ts")

def getActionName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Action")

def getActionReturnType(method, fileName, catName):
    if method.lower() == "get" and fileName.lower() == "index":
        return getActionName(catName, fileName) + "Ret|ErrorDB"
    if method.lower() == "get" and fileName.lower() == "show":
        return getModelFileNameFromCatName(catName)[:-3] + "|ErrorDB"
    return "null|ErrorDB"

