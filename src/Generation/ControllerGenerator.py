from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import CONTROLLER_CONTROLLER_DTO_BLOCK_PATH, CONTROLLER_TEMPLATE_PATH, CONTROLLER_DTO_IMPORT_TEMPLATE_PATH, DTO_ASYNC_TEMPLATE_PATH
from .TemplatesPaths import CONTROLLER_ACTION_IMPORT_TEMPLATE_PATH, CONTROLLER_MODEL_IMPORT_TEMPLATE_PATH
from .TemplatesPaths import CONTROLLER_CONTROLLER_TEMPLATE_PATH, CONTROLLER_CONTROLLER_DB_ERROR_RES_TEMPLATE_PATH, CONTROLLER_CONTROLLER_DTO_ERROR_RES_TEMPLATE_PATH
from .TemplatesPaths import CONTROLLER_CONTROLLER_GET_RES_TEMPLATE_PATH, CONTROLLER_CONTROLLER_PUT_RES_TEMPLATE_PATH
from .TemplatesPaths import CONTROLLER_CONTROLLER_POST_RES_TEMPLATE_PATH, CONTROLLER_CONTROLLER_DELETE_RES_TEMPLATE_PATH
from .Flags import CONTROLLER_ACTION_IMPORTS, CONTROLLER_CONTROLLER_DTO_BLOCK_PLACE, CONTROLLER_CONTROLLER_DTO_VAR_NAME, CONTROLLER_DTO_IMPORTS, CONTROLLER_DTO_IMPORT_FILE_NAME, CONTROLLER_DTO_IMPORT_DTO_NAMES, DTO_ASYNC_PLACEHOLDER
from .Flags import CONTROLLER_ACTION_IMPORT_FILE_NAME, CONTROLLER_ACTION_IMPORT_ACTION_NAMES, CONTROLLER_MODEL_IMPORTS
from .Flags import CONTROLLER_MODEL_IMPORT_MODEL_NAME, CONTROLLER_MODEL_IMPORT_FILE_NAME, CONTROLLER_PLACEHOLDER
from .Flags import CONTROLLER_CONTROLLER_NAME, CONTROLLER_CONTROLLER_DTO_FUNC_NAME, CONTROLLER_CONTROLLER_DTO_STRUC_NAME
from .Flags import CONTROLLER_CONTROLLER_ACTION_NAME, CONTROLLER_CONTROLLER_ACTION_RET_TYPE, CONTROLLER_CONTROLLER_SUCESS_RES
from .Flags import CONTROLLER_CONTROLLER_DB_ERROR_RES, CONTROLLER_CONTROLLER_DTO_ERROR_RES
from .DTOGenerator import doesNeedDTO, getDTOFileName, getDTOStrucName, getDTOFuncName, getDTOVarName
from .ActionGenerator import getActionFileName, getActionName, getActionReturnType
from .ModelGenerator import getModelFileNameFromTargetTable

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
        self.actionName = getActionName(self.catName, self.srcFileName[:-5])
        self.actionReturnType = getActionReturnType(self.method, self.srcFileName[:-5], self.json.access('targetTable')).split('|')
        self.DTOFuncName = getDTOFuncName(self.catName, self.srcFileName[:-5])
        self.DTOStrucName = getDTOStrucName(self.catName, self.srcFileName[:-5])
        self.modelFileName = getModelFileNameFromTargetTable(self.json.access('targetTable'))[:-3]
        print('\nSetup Controller generator\n', self.distFile, "\n")


    def importDTOs(self):
        self.template = self.template.replace(CONTROLLER_DTO_IMPORTS, readFile(CONTROLLER_DTO_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(CONTROLLER_DTO_IMPORT_FILE_NAME, getDTOFileName(self.catName)[:-3])
        importsBloc = self.DTOStrucName + ", " + self.DTOFuncName
        self.template = self.template.replace(CONTROLLER_DTO_IMPORT_DTO_NAMES, importsBloc + ", " + CONTROLLER_DTO_IMPORT_DTO_NAMES)


    def importActions(self):
        self.template = self.template.replace(CONTROLLER_ACTION_IMPORTS, readFile(CONTROLLER_ACTION_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(CONTROLLER_ACTION_IMPORT_FILE_NAME, getActionFileName(self.catName)[:-3])
        fileName = self.srcFileName[:-5]
        importsBloc = self.actionName
        if (self.method.lower() == "get" and fileName.lower() == "index") or (self.method.lower() == "post" and fileName.lower() == "create"):
            importsBloc += ", " + self.actionReturnType[0]
        if self.method.lower() == "get" and fileName.lower() == "show":
            self.template = self.template.replace(CONTROLLER_MODEL_IMPORTS, readFile(CONTROLLER_MODEL_IMPORT_TEMPLATE_PATH))
            self.template = self.template.replace(CONTROLLER_MODEL_IMPORT_FILE_NAME, self.modelFileName)
            self.template = self.template.replace(CONTROLLER_MODEL_IMPORT_MODEL_NAME, self.actionReturnType[0])
        self.template = self.template.replace(CONTROLLER_ACTION_IMPORT_ACTION_NAMES, importsBloc + ", " + CONTROLLER_ACTION_IMPORT_ACTION_NAMES)


    def getMethodResTemplate(self):
        methodLowered = self.method.lower()
        rets = [
            ["get", CONTROLLER_CONTROLLER_GET_RES_TEMPLATE_PATH],
            ["put", CONTROLLER_CONTROLLER_PUT_RES_TEMPLATE_PATH],
            ["post", CONTROLLER_CONTROLLER_POST_RES_TEMPLATE_PATH],
            ["delete", CONTROLLER_CONTROLLER_DELETE_RES_TEMPLATE_PATH]
        ]
        for elem in rets:
            if elem[0] == methodLowered:
                return elem[1]
        return CONTROLLER_CONTROLLER_GET_RES_TEMPLATE_PATH

    def generateControllers(self):
        ret = ""
        ret += readFile(CONTROLLER_CONTROLLER_TEMPLATE_PATH)
        ret = ret.replace(CONTROLLER_CONTROLLER_NAME, self.srcFileName[:-5])
        if doesNeedDTO(self.json):
            ret = ret.replace(CONTROLLER_CONTROLLER_DTO_VAR_NAME, getDTOVarName(self.catName, self.srcFileName[:-5]))
            ret = ret.replace(CONTROLLER_CONTROLLER_DTO_BLOCK_PLACE, readFile(CONTROLLER_CONTROLLER_DTO_BLOCK_PATH))
        ret = ret.replace(CONTROLLER_CONTROLLER_DTO_FUNC_NAME, self.DTOFuncName)
        ret = ret.replace(CONTROLLER_CONTROLLER_DTO_STRUC_NAME, self.DTOStrucName)
        ret = ret.replace(CONTROLLER_CONTROLLER_ACTION_NAME, self.actionName)
        ret = ret.replace(CONTROLLER_CONTROLLER_ACTION_RET_TYPE, "|".join(self.actionReturnType))
        ret = ret.replace(CONTROLLER_CONTROLLER_SUCESS_RES, readFile(self.getMethodResTemplate()))
        ret = ret.replace(CONTROLLER_CONTROLLER_DB_ERROR_RES, readFile(CONTROLLER_CONTROLLER_DB_ERROR_RES_TEMPLATE_PATH))
        ret = ret.replace(CONTROLLER_CONTROLLER_DTO_ERROR_RES, readFile(CONTROLLER_CONTROLLER_DTO_ERROR_RES_TEMPLATE_PATH))
        return ret


    def replaceFlags(self):
        if doesNeedDTO(self.json):
            self.importDTOs()
        self.importActions()
        generatedController = self.generateControllers()
        if " await " in generatedController:
            generatedController = generatedController.replace(DTO_ASYNC_PLACEHOLDER, readFile(DTO_ASYNC_TEMPLATE_PATH))
        self.template = self.template.replace(CONTROLLER_PLACEHOLDER, generatedController)
        return

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Controller generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)