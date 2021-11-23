from ..Tools.CaseHandler import toCodeCamelCase
from .ModelGenerator import getModelFileNameFromCatName

def getActionFileName(catName):
    return toCodeCamelCase(catName + "Action.ts")

def getActionName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Action")

def getActionReturnType(method, fileName, catName, actionName):
    if method.lower() == "get" and fileName.lower() == "index":
        return getActionName(catName, actionName) + "Ret|ErrorDB"
    if method.lower() == "get":
        return getModelFileNameFromCatName(catName)[:-3] + "|ErrorDB"
    return "null|ErrorDB"

