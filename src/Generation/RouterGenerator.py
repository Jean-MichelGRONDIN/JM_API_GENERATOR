from .Flags import ROUTER_MIDDLEWARE_IMPORTS, ROUTER_SANITIZER_IMPORTS, ROUTER_VALIDATOR_IMPORTS, ROUTER_CONTROLLER_IMPORTS, ROUTER_ROUTES, ROUTER_MIDDLEWARE_IMPORT_NAME, ROUTER_SANITIZER_IMPORT_FILE_NAME, ROUTER_SANITIZER_IMPORT_SANITIZER_NAME, ROUTER_VALIDATOR_IMPORT_FILE_NAME, ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME
from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import ROUTER_TEMPLATE_PATH, ROUTER_MIDDLEWARE_IMPORT_TEMPLATE_PATH, ROUTER_SANITIZER_IMPORT_TEMPLATE_PATH, ROUTER_VALIDATOR_IMPORT_TEMPLATE_PATH
from .SanitizerGenerator import getSanitiZerFileName, getSanitiZerMiddlewareName
from .ValidatorGenerator import getValidatorFileName, getValidatorMiddlewareName
from .ControllerGenerator import getControllerFileName, getControllerMiddlewareName

class RouterGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = toCodeCamelCase(self.catName)
        self.distFile = self.distPath + self.fileName + "Router.ts"
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, ROUTER_TEMPLATE_PATH)
        print('\nSetup Router generator\n', self.distFile, "\n")


    def importMiddlewares(self):
        data = ""
        list = self.json.access('middlewares')
        for elem in list:
            data += readFile(ROUTER_MIDDLEWARE_IMPORT_TEMPLATE_PATH)
            data += "\n"
            data = data.replace(ROUTER_MIDDLEWARE_IMPORT_NAME, elem)
        if data in self.template:
            data = ""
        data += ROUTER_MIDDLEWARE_IMPORTS
        return data


    def hasSanitizer(self):
        data = self.json.access('data')
        for elem in data:
            elemJson = JsonHandler(elem)
            if elemJson.access('sanitizer.has'):
                return True
        return False

    def importSanitizer(self):
        self.template = self.template.replace(ROUTER_SANITIZER_IMPORTS, readFile(ROUTER_SANITIZER_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(ROUTER_SANITIZER_IMPORT_FILE_NAME, getSanitiZerFileName(self.catName)[:-3])
        self.template = self.template.replace(ROUTER_SANITIZER_IMPORT_SANITIZER_NAME, getSanitiZerMiddlewareName(self.catName, self.srcFileName[:-5]) + ", " + ROUTER_SANITIZER_IMPORT_SANITIZER_NAME)


    def hasValidator(self):
        data = self.json.access('data')
        for elem in data:
            elemJson = JsonHandler(elem)
            if elemJson.access('validator.has'):
                return True
        return False

    def importValidator(self):
        self.template = self.template.replace(ROUTER_VALIDATOR_IMPORTS, readFile(ROUTER_VALIDATOR_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(ROUTER_VALIDATOR_IMPORT_FILE_NAME, getValidatorFileName(self.catName)[:-3])
        self.template = self.template.replace(ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME, getValidatorMiddlewareName(self.catName, self.srcFileName[:-5]) + ", " + ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME)


    def replaceFlags(self):
        print(self.template)
        self.template = self.template.replace(ROUTER_MIDDLEWARE_IMPORTS, self.importMiddlewares())
        if self.hasSanitizer():
            self.importSanitizer()
        if self.hasValidator():
            self.importValidator()
        # self.template = self.template.replace(ROUTER_CONTROLLER_IMPORTS, self.fileName)
        self.template = self.template.replace(ROUTER_ROUTES, self.srcFileName[:-5] + "\n" + ROUTER_ROUTES)

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Router generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

