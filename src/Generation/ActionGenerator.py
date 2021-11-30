from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import ACTION_TEMPLATE_PATH, ACTION_DTO_IMPORT_TEMPLATE_PATH, ACTION_MODEL_IMPORT_TEMPLATE_PATH
from .TemplatesPaths import ACTION_INDEX_TEMPLATE_PATH, ACTION_CREATE_TEMPLATE_PATH, ACTION_UPDATE_TEMPLATE_PATH, ACTION_SHOW_TEMPLATE_PATH, ACTION_DESTROY_TEMPLATE_PATH
from .Flags import ACTION_DTO_IMPORTS, ACTION_DTO_IMPORT_FILE_NAME, ACTION_DTO_IMPORT_DTO_NAME, ACTION_PLACEHOLDER
from .Flags import ACTION_MODEL_IMPORTS, ACTION_MODEL_IMPORT_FILE_NAME, ACTION_MODEL_IMPORT_MODEL_NAME
from .DTOGenerator import getDTOFileName, getDTOStrucName
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



class ActionGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = getActionFileName(self.catName)
        self.distFile = self.distPath + self.fileName
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, ACTION_TEMPLATE_PATH)
        self.method = self.json.access('method')
        self.actionName = getActionName(self.catName, self.srcFileName[:-5])
        self.actionReturnType = getActionReturnType(self.method, self.srcFileName[:-5], self.json.access('targetTable')).split('|')
        self.DTOStrucName = getDTOStrucName(self.catName, self.srcFileName[:-5])
        self.modelFileName = getModelFileNameFromTargetTable(self.json.access('targetTable'))
        print('\nSetup Action generator\n', self.distFile, "\n")


    def importDTOs(self):
        self.template = self.template.replace(ACTION_DTO_IMPORTS, readFile(ACTION_DTO_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(ACTION_DTO_IMPORT_FILE_NAME, getDTOFileName(self.catName)[:-3])
        self.template = self.template.replace(ACTION_DTO_IMPORT_DTO_NAME, self.DTOStrucName + ", " + ACTION_DTO_IMPORT_DTO_NAME)
        return


    def importModels(self):
        ret = ""
        if self.method.lower() == "get":
            bloc = readFile(ACTION_MODEL_IMPORT_TEMPLATE_PATH)
            bloc = ret.replace(ACTION_MODEL_IMPORT_FILE_NAME, self.modelFileName)
            bloc = ret.replace(ACTION_MODEL_IMPORT_MODEL_NAME, self.modelFileName[:-3])
            if bloc not in self.template:
                ret = bloc
        return ret


    def generateActions(self):
        ret = ""
        ret += readFile(ACTION_CREATE_TEMPLATE_PATH)
        return ret


    def replaceFlags(self):
        self.template = self.template.replace(ACTION_MODEL_IMPORTS, self.importModels())
        self.importDTOs()
        self.template = self.template.replace(ACTION_PLACEHOLDER, self.generateActions())
        return

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Action generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)