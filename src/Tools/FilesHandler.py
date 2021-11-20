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

def writeInFile(name, data):
    chekfile = basename(name)
    if (chekfile != ''):
        with open(name, 'w+') as f:
            f.write(data)

def createFile(name):
    writeInFile(name, "")

def creatFileByPath(path, data):
    file = path
    folders = dirname(path)
    createFolder(folders)
    createFile(file)

def basename(str):
    return path.basename(str)

def dirname(str):
    return path.dirname(str)