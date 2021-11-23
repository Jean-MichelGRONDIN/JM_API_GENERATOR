from ..Tools.CaseHandler import toCodeCamelCase

def getSanitiZerFileName(catName):
    return toCodeCamelCase(catName + "Sanitizer.ts")
