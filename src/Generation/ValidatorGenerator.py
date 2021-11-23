from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import VALIDATOR_TEMPLATE_PATH, VALIDATOR_MIDDLEWARE_TEMPLATE_PATH, VALIDATOR_MIDDLEWARE_RULES_TEMPLATE_PATH
from .Flags import VALIDATOR_MIDDLEWARES, VALIDATOR_MIDDLEWARE_NAME, VALIDATOR_MIDDLEWARE_RULES, VALIDATOR_MIDDLEWARE_RULE_NAME, VALIDATOR_MIDDLEWARE_RULE_VALUE

def getValidatorFileName(catName):
    return toCodeCamelCase(catName + "Validator.ts")

def getValidatorMiddlewareName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Validator")

def hasValidator(json):
    data = json.access('data')
    for elem in data:
        elemJson = JsonHandler(elem)
        if elemJson.access('validator.has'):
            return True
    return False


class ValidatorGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = getValidatorFileName(self.catName)
        self.distFile = self.distPath + self.fileName
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, VALIDATOR_TEMPLATE_PATH)
        print('\nSetup Validator generator\n', self.distFile, "\n")


    def generateValidator(self):
        ret = ""
        ret += readFile(VALIDATOR_MIDDLEWARE_TEMPLATE_PATH)
        ret = ret.replace(VALIDATOR_MIDDLEWARE_NAME, getValidatorMiddlewareName(self.catName, self.srcFileName[:-5]))
        data = self.json.access('data')
        for elem in data:
            elemJson = JsonHandler(elem)
            if elemJson.access('sanitizer.has'):
                ret = ret.replace(VALIDATOR_MIDDLEWARE_RULES, readFile(VALIDATOR_MIDDLEWARE_RULES_TEMPLATE_PATH))
                ret = ret.replace(VALIDATOR_MIDDLEWARE_RULE_NAME, elemJson.access('name'))
                ret = ret.replace(VALIDATOR_MIDDLEWARE_RULE_VALUE, elemJson.access('validator.rule'))
        ret = ret.replace(VALIDATOR_MIDDLEWARE_RULES, "")
        return ret

    def replaceFlags(self):
        self.template = self.template.replace(VALIDATOR_MIDDLEWARES, self.generateValidator())

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Validator generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

