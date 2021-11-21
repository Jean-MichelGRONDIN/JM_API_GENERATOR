from os import listdir, makedirs
from os.path import isfile, isdir, join, basename, dirname
from json import loads

def getDirFolders(path):
    folders = [f for f in listdir(path) if isdir(join(path, f))]
    return folders

def getDirFiles(path):
    files = [f for f in listdir(path) if isfile(join(path, f)) and f[-5:] == '.json']
    return files

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
    return basename(str)

def dirname(str):
    return dirname(str)

