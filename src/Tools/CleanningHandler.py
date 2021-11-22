from .FilesHandler import readFile, writeInFile
from re import sub

def replaceTabsBySpaces(data):
    data = sub(r'\t', '    ', data)
    return data

def cleanTags(data):
    data = sub(r'\$[A-Z,_]+\$', '', data)
    return data

def cleanLongLineReturnChains(data):
    data = sub(r'\n\n[\n]+', '\n\n', data)
    return data

def cleanDuplicatedLineReturns(data):
    data = sub(r'\n[\n]+', '\n', data)
    return data

def cleanLongLineReturnBeforeDotComma(data):
    data = sub(r'[\n]+;', ';', data)
    return data


def cleanModelFile(filePath):
    cleanningSteps = [
        replaceTabsBySpaces,
        cleanTags,
        cleanDuplicatedLineReturns
    ]
    content = readFile(filePath)
    for step in cleanningSteps:
        content = step(content)
    writeInFile(filePath, content)

def cleanMigrationFile(filePath):
    cleanningSteps = [
        replaceTabsBySpaces,
        cleanTags,
        cleanLongLineReturnChains,
        cleanLongLineReturnBeforeDotComma
    ]
    content = readFile(filePath)
    for step in cleanningSteps:
        content = step(content)
    writeInFile(filePath, content)