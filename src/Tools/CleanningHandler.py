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

def cleanMultiplesLineReturnBetweenImports(data):
    data = sub(r'\n[\n, ]+import', '\nimport', data)
    return data

def cleanEndOfImportComma(data):
    data = sub(r',[ ]+}', ' }', data)
    return data


def cleanFile(filePath, rules):
    content = readFile(filePath)
    for step in rules:
        content = step(content)
    writeInFile(filePath, content)


def cleanModelFile(filePath):
    rules = [
        replaceTabsBySpaces,
        cleanTags,
        cleanDuplicatedLineReturns
    ]
    cleanFile(filePath, rules)

def cleanMigrationFile(filePath):
    rules = [
        replaceTabsBySpaces,
        cleanTags,
        cleanLongLineReturnChains,
        cleanLongLineReturnBeforeDotComma
    ]
    cleanFile(filePath, rules)

def cleanRouterFile(filePath):
    rules = [
        replaceTabsBySpaces,
        cleanTags,
        cleanLongLineReturnChains,
        cleanMultiplesLineReturnBetweenImports,
        cleanEndOfImportComma
    ]
    cleanFile(filePath, rules)
