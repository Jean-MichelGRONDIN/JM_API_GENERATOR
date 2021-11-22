from .FilesHandler import readFile, writeInFile
from re import sub

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
        cleanTags,
        cleanDuplicatedLineReturns
    ]
    content = readFile(filePath)
    for step in cleanningSteps:
        content = step(content)
    writeInFile(filePath, content)

def cleanMigrationFile(filePath):
    cleanningSteps = [
        cleanTags,
        cleanLongLineReturnChains,
        cleanLongLineReturnBeforeDotComma
    ]
    content = readFile(filePath)
    for step in cleanningSteps:
        content = step(content)
    writeInFile(filePath, content)