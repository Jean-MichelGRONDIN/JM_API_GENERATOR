from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import CONTROLLER_TEMPLATE_PATH, CONTROLLER_DTO_IMPORT_TEMPLATE_PATH
from .TemplatesPaths import CONTROLLER_ACTION_IMPORT_TEMPLATE_PATH, CONTROLLER_MODEL_IMPORT_TEMPLATE_PATH
from .Flags import CONTROLLER_ACTION_IMPORTS, CONTROLLER_DTO_IMPORTS, CONTROLLER_DTO_IMPORT_FILE_NAME, CONTROLLER_DTO_IMPORT_DTO_NAMES
from .Flags import CONTROLLER_ACTION_IMPORT_FILE_NAME, CONTROLLER_ACTION_IMPORT_ACTION_NAMES, CONTROLLER_MODEL_IMPORTS
from .Flags import CONTROLLER_MODEL_IMPORT_MODEL_NAME, CONTROLLER_MODEL_IMPORT_FILE_NAME
from .DTOGenerator import getDTOFileName, getDTOStrucName, getDTOFuncName
from .ActionGenerator import getActionFileName, getActionName, getActionReturnType
from .ModelGenerator import getModelFileNameFromCatName

def getControllerFileName(catName):
    return toCodeCamelCase(catName + ".controller.ts")


def getControllerMiddlewareName(actionName):
    return toCodeCamelCase(actionName)



class ControllerGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = getControllerFileName(self.catName)
        self.distFile = self.distPath + self.fileName
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, CONTROLLER_TEMPLATE_PATH)
        self.method = self.json.access('method')
        self.actionReturnType = getActionReturnType(self.method, self.srcFileName[:-5], self.catName).split('|')
        print('\nSetup Controller generator\n', self.distFile, "\n")


    def importDTOs(self):
        self.template = self.template.replace(CONTROLLER_DTO_IMPORTS, readFile(CONTROLLER_DTO_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(CONTROLLER_DTO_IMPORT_FILE_NAME, getDTOFileName(self.catName)[:-3])
        importsBloc = getDTOStrucName(self.catName, self.srcFileName[:-5]) + ", " + getDTOFuncName(self.catName, self.srcFileName[:-5])
        self.template = self.template.replace(CONTROLLER_DTO_IMPORT_DTO_NAMES, importsBloc + ", " + CONTROLLER_DTO_IMPORT_DTO_NAMES)


    def importActions(self):
        self.template = self.template.replace(CONTROLLER_ACTION_IMPORTS, readFile(CONTROLLER_ACTION_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(CONTROLLER_ACTION_IMPORT_FILE_NAME, getActionFileName(self.catName)[:-3])
        importsBloc = getActionName(self.catName, self.srcFileName[:-5])
        fileName = self.srcFileName[:-5]
        if self.method.lower() == "get" and fileName.lower() == "index":
            importsBloc += ", " + self.actionReturnType[0]
        if self.method.lower() == "get" and fileName.lower() == "show":
            self.template = self.template.replace(CONTROLLER_MODEL_IMPORTS, readFile(CONTROLLER_MODEL_IMPORT_TEMPLATE_PATH))
            self.template = self.template.replace(CONTROLLER_MODEL_IMPORT_FILE_NAME, getModelFileNameFromCatName(self.catName)[:-3])
            self.template = self.template.replace(CONTROLLER_MODEL_IMPORT_MODEL_NAME, getModelFileNameFromCatName(self.catName)[:-3])
        self.template = self.template.replace(CONTROLLER_ACTION_IMPORT_ACTION_NAMES, importsBloc + ", " + CONTROLLER_ACTION_IMPORT_ACTION_NAMES)


    def replaceFlags(self):
        print(self.srcFileName)
        self.importDTOs()
        self.importActions()
        return

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Controller generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)