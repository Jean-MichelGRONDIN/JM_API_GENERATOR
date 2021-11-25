from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import CONTROLLER_TEMPLATE_PATH, CONTROLLER_DTO_IMPORT_TEMPLATE_PATH
from .Flags import CONTROLLER_ACTION_IMPORTS, CONTROLLER_DTO_IMPORTS, CONTROLLER_DTO_IMPORT_FILE_NAME, CONTROLLER_DTO_IMPORT_DTO_NAMES
from .DTOGenerator import getDTOFileName, getDTOStrucName, getDTOFuncName

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
        print('\nSetup Controller generator\n', self.distFile, "\n")


    def importDTOs(self):#CONTROLLER_ACTION_IMPORTS
        self.template = self.template.replace(CONTROLLER_DTO_IMPORTS, readFile(CONTROLLER_DTO_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(CONTROLLER_DTO_IMPORT_FILE_NAME, getDTOFileName(self.catName)[:-3])
        importsBloc = getDTOStrucName(self.catName, self.srcFileName[:-5]) + ", " + getDTOFuncName(self.catName, self.srcFileName[:-5])
        self.template = self.template.replace(CONTROLLER_DTO_IMPORT_DTO_NAMES, importsBloc + ", " + CONTROLLER_DTO_IMPORT_DTO_NAMES)


    # def importActions(self):
    #     self.template = self.template.replace(ROUTER_VALIDATOR_IMPORTS, readFile(ROUTER_VALIDATOR_IMPORT_TEMPLATE_PATH))
    #     self.template = self.template.replace(ROUTER_VALIDATOR_IMPORT_FILE_NAME, getValidatorFileName(self.catName)[:-3])
    #     self.template = self.template.replace(ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME, getValidatorMiddlewareName(self.catName, self.srcFileName[:-5]) + ", " + ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME)


    def replaceFlags(self):
        self.importDTOs()
        # self.importActions()
        return

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Controller generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)