from ..Tools.CaseHandler import toCodeCamelCase

def getDTOFileName(catName):
    return toCodeCamelCase(catName + "Data.ts")

def getDTOStrucName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Data")

def getDTOFuncName(catName, actionName):
    return getDTOStrucName(catName, actionName) + "FromRequest"

