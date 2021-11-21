from os import makedirs, path
from json import loads


def createFolder(path):
    makedirs(path, exist_ok=True)

def readFile(path):
    f = open(path, "r")
    return f.read()

def readJsonFile(path):
    file = readFile(path)
    return loads(file)

def writeInFile(path, data):
    with open(path, 'w+') as f:
        f.truncate()
        f.write(data)

def writeInFileByPath(path, data):
    file = path
    folders = dirname(path)
    createFolder(folders)
    writeInFile(file, data)

def createFile(name):
    writeInFile(name, "")

def creatFileByPath(path):
    writeInFileByPath(path, "")

def basename(str):
    return path.basename(str)

def dirname(str):
    return path.dirname(str)