from ..Tools.CaseHandler import toCodeCamelCase
from .ModelGenerator import getModelFileNameFromTargetTable

def getActionFileName(catName):
    return toCodeCamelCase(catName + "Action.ts")

def getActionName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Action")

def getActionReturnType(method, fileName, targetTable):
    if method.lower() == "get" and fileName.lower() == "index":
        return getActionName(targetTable, fileName) + "Ret|ErrorDB"
    if method.lower() == "get" and fileName.lower() == "show":
        return getModelFileNameFromTargetTable(targetTable)[:-3] + "|ErrorDB"
    return "null|ErrorDB"

