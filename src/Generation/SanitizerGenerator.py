from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import SANITIZER_TEMPLATE_PATH, SANITIZER_MIDDLEWARE_TEMPLATE_PATH, SANITIZER_MIDDLEWARE_RULES_TEMPLATE_PATH
from .Flags import SANITIZER_MIDDLEWARES, SANITIZER_MIDDLEWARE_NAME, SANITIZER_MIDDLEWARE_RULES, SANITIZER_MIDDLEWARE_RULE_NAME, SANITIZER_MIDDLEWARE_RULE_VALUE

def getSanitiZerFileName(catName):
    return toCodeCamelCase(catName + "Sanitizer.ts")

def getSanitiZerMiddlewareName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Sanitizer")

def hasSanitizer(json):
    data = json.access('data')
    for elem in data:
        elemJson = JsonHandler(elem)
        if elemJson.access('sanitizer.has'):
            return True
    return False


class SanitizerGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = getSanitiZerFileName(self.catName)
        self.distFile = self.distPath + self.fileName
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, SANITIZER_TEMPLATE_PATH)
        print('\nSetup Sanitizer generator\n', self.distFile, "\n")


    def generateSanitizer(self):
        ret = ""
        ret += readFile(SANITIZER_MIDDLEWARE_TEMPLATE_PATH)
        ret = ret.replace(SANITIZER_MIDDLEWARE_NAME, getSanitiZerMiddlewareName(self.catName, self.srcFileName[:-5]))
        data = self.json.access('data')
        for elem in data:
            elemJson = JsonHandler(elem)
            if elemJson.access('sanitizer.has'):
                ret = ret.replace(SANITIZER_MIDDLEWARE_RULES, readFile(SANITIZER_MIDDLEWARE_RULES_TEMPLATE_PATH))
                ret = ret.replace(SANITIZER_MIDDLEWARE_RULE_NAME, elemJson.access('name'))
                ret = ret.replace(SANITIZER_MIDDLEWARE_RULE_VALUE, elemJson.access('sanitizer.rule'))
        ret = ret.replace(SANITIZER_MIDDLEWARE_RULES, "")
        return ret

    def replaceFlags(self):
        self.template = self.template.replace(SANITIZER_MIDDLEWARES, self.generateSanitizer())

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Sanitizer generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)



