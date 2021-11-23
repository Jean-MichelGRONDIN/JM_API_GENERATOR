from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import DTO_TEMPLATE_PATH, DTO_DUO_TEMPLATE_PATH#SANITIZER_TEMPLATE_PATH, SANITIZER_MIDDLEWARE_TEMPLATE_PATH, SANITIZER_MIDDLEWARE_RULES_TEMPLATE_PATH
from .Flags import DTO_PLACEHOLDER, DTO_STRUC_NAME, DTO_FUNC_NAME#SANITIZER_MIDDLEWARES, SANITIZER_MIDDLEWARE_NAME, SANITIZER_MIDDLEWARE_RULES, SANITIZER_MIDDLEWARE_RULE_NAME, SANITIZER_MIDDLEWARE_RULE_VALUE

def getDTOFileName(catName):
    return toCodeCamelCase(catName + "Data.ts")

def getDTOStrucName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Data")

def getDTOFuncName(catName, actionName):
    return getDTOStrucName(catName, actionName) + "FromRequest"


class DTOGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = getDTOFileName(self.catName)
        self.distFile = self.distPath + self.fileName
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, DTO_TEMPLATE_PATH)
        print('\nSetup DTO generator\n', self.distFile, "\n")


    def generateDTO(self):
        ret = ""
        ret += readFile(DTO_DUO_TEMPLATE_PATH)
        ret = ret.replace(DTO_STRUC_NAME, getDTOStrucName(self.catName, self.srcFileName[:-5]))
        ret = ret.replace(DTO_FUNC_NAME, getDTOFuncName(self.catName, self.srcFileName[:-5]))
        # data = self.json.access('data')
        # for elem in data:
        #     elemJson = JsonHandler(elem)
        #     if elemJson.access('sanitizer.has'):
        #         ret = ret.replace(SANITIZER_MIDDLEWARE_RULES, readFile(SANITIZER_MIDDLEWARE_RULES_TEMPLATE_PATH))
        #         ret = ret.replace(SANITIZER_MIDDLEWARE_RULE_NAME, elemJson.access('name'))
        #         ret = ret.replace(SANITIZER_MIDDLEWARE_RULE_VALUE, elemJson.access('sanitizer.rule'))
        # ret = ret.replace(SANITIZER_MIDDLEWARE_RULES, "")
        return ret

    def replaceFlags(self):
        self.template = self.template.replace(DTO_PLACEHOLDER, self.generateDTO())

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun DTO generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)