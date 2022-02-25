from .Flags import ROUTER_MIDDLEWARE_IMPORTS, ROUTER_ROUTE_SANITIZER_CALL, ROUTER_ROUTE_VALIDATOR_CALL, ROUTER_SANITIZER_IMPORTS, ROUTER_VALIDATOR_IMPORTS, ROUTER_CONTROLLER_IMPORTS, ROUTER_ROUTES
from .Flags import ROUTER_MIDDLEWARE_IMPORT_NAME, ROUTER_SANITIZER_IMPORT_FILE_NAME, ROUTER_SANITIZER_IMPORT_SANITIZER_NAME, ROUTER_VALIDATOR_IMPORT_FILE_NAME
from .Flags import ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME, ROUTER_CONTROLLER_IMPORT_FILE_NAME, ROUTER_CONTROLLER_IMPORT_SANITIZER_NAME
from .Flags import ROUTER_ROUTE_TYPE, ROUTER_ROUTE_TITLE, ROUTER_ROUTE_DESCRIPTION, ROUTER_ROUTE_TYPE_CALL, ROUTER_ROUTE_CAT_NAME, ROUTER_ROUTE_PARAM_FIELD
from .Flags import ROUTER_ROUTE_PARAM_NAME, ROUTER_ROUTE_MIDDLEWARE_CALL, ROUTER_ROUTE_CONTROLLER_CALL, ROUTER_ROUTE_MIDDLEWARE_NAME
from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import ROUTER_SANITIZER_CALL_TEMPLATE_PATH, ROUTER_TEMPLATE_PATH, ROUTER_MIDDLEWARE_IMPORT_TEMPLATE_PATH, ROUTER_SANITIZER_IMPORT_TEMPLATE_PATH, ROUTER_VALIDATOR_CALL_TEMPLATE_PATH
from .TemplatesPaths import ROUTER_VALIDATOR_IMPORT_TEMPLATE_PATH, ROUTER_CONTROLLER_IMPORT_TEMPLATE_PATH, ROUTER_ROUTE_TEMPLATE_PATH
from .TemplatesPaths import ROUTER_ROUTE_PARAM_TEMPLATE_PATH, ROUTER_ROUTE_MIDDLEWARE_TEMPLATE_PATH
from .SanitizerGenerator import getSanitiZerFileName, getSanitiZerMiddlewareName, hasSanitizer
from .ValidatorGenerator import getValidatorFileName, getValidatorMiddlewareName, hasValidator
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


    def importSanitizer(self):
        self.template = self.template.replace(ROUTER_SANITIZER_IMPORTS, readFile(ROUTER_SANITIZER_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(ROUTER_SANITIZER_IMPORT_FILE_NAME, getSanitiZerFileName(self.catName)[:-3])
        self.template = self.template.replace(ROUTER_SANITIZER_IMPORT_SANITIZER_NAME, getSanitiZerMiddlewareName(self.catName, self.srcFileName[:-5]) + ", " + ROUTER_SANITIZER_IMPORT_SANITIZER_NAME)

    def callSanitizer(self, data):
        data = data.replace(ROUTER_ROUTE_SANITIZER_CALL, readFile(ROUTER_SANITIZER_CALL_TEMPLATE_PATH))
        data = data.replace(ROUTER_SANITIZER_IMPORT_SANITIZER_NAME, getSanitiZerMiddlewareName(self.catName, self.srcFileName[:-5]))
        return data


    def importValidator(self):
        self.template = self.template.replace(ROUTER_VALIDATOR_IMPORTS, readFile(ROUTER_VALIDATOR_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(ROUTER_VALIDATOR_IMPORT_FILE_NAME, getValidatorFileName(self.catName)[:-3])
        self.template = self.template.replace(ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME, getValidatorMiddlewareName(self.catName, self.srcFileName[:-5]) + ", " + ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME)

    def callValidator(self, data):
        data = data.replace(ROUTER_ROUTE_VALIDATOR_CALL, readFile(ROUTER_VALIDATOR_CALL_TEMPLATE_PATH))
        data = data.replace(ROUTER_VALIDATOR_IMPORT_VALIDATOR_NAME, getValidatorMiddlewareName(self.catName, self.srcFileName[:-5]))
        return data


    def importController(self):
        self.template = self.template.replace(ROUTER_CONTROLLER_IMPORTS, readFile(ROUTER_CONTROLLER_IMPORT_TEMPLATE_PATH))
        self.template = self.template.replace(ROUTER_CONTROLLER_IMPORT_FILE_NAME, getControllerFileName(self.catName)[:-3])
        self.template = self.template.replace(ROUTER_CONTROLLER_IMPORT_SANITIZER_NAME, getControllerMiddlewareName(self.srcFileName[:-5]) + ", " + ROUTER_CONTROLLER_IMPORT_SANITIZER_NAME)


    def generateRouteParams(self, ret):
        data = self.json.access('data')
        for elem in data:
            elemJson = JsonHandler(elem)
            if elemJson.access('get.from') == "params":
                ret = ret.replace(ROUTER_ROUTE_PARAM_FIELD, readFile(ROUTER_ROUTE_PARAM_TEMPLATE_PATH))
                ret = ret.replace(ROUTER_ROUTE_PARAM_NAME, elemJson.access('name'))
        ret = ret.replace(ROUTER_ROUTE_PARAM_FIELD, "")
        return ret

    def generateRouteMiddlewares(self, ret):
        middlewares = self.json.access('middlewares')
        for elem in middlewares:
            ret = ret.replace(ROUTER_ROUTE_MIDDLEWARE_CALL, readFile(ROUTER_ROUTE_MIDDLEWARE_TEMPLATE_PATH))
            ret = ret.replace(ROUTER_ROUTE_MIDDLEWARE_NAME, elem)
        ret = ret.replace(ROUTER_ROUTE_MIDDLEWARE_CALL, "")
        return ret

    def generateRoute(self):
        data = ""
        data += readFile(ROUTER_ROUTE_TEMPLATE_PATH)
        data = data.replace(ROUTER_ROUTE_TYPE, self.json.access('method').upper())
        data = data.replace(ROUTER_ROUTE_TITLE, self.json.access('title'))
        data = data.replace(ROUTER_ROUTE_DESCRIPTION, self.json.access('description'))
        data = data.replace(ROUTER_ROUTE_TYPE_CALL, self.json.access('method').lower())
        data = data.replace(ROUTER_ROUTE_CAT_NAME, toCodeCamelCase(self.srcFileName[:-5]))
        data = self.generateRouteParams(data)
        data = self.generateRouteMiddlewares(data)
        if hasSanitizer(self.json):
            data = self.callSanitizer(data)
        if hasValidator(self.json):
            data = self.callValidator(data)
        data = data.replace(ROUTER_ROUTE_CONTROLLER_CALL, getControllerMiddlewareName(self.srcFileName[:-5]))
        data += "\n\n"
        data += ROUTER_ROUTES
        return data


    def replaceFlags(self):
        self.template = self.template.replace(ROUTER_MIDDLEWARE_IMPORTS, self.importMiddlewares())
        if hasSanitizer(self.json):
            self.importSanitizer()
        if hasValidator(self.json):
            self.importValidator()
        self.importController()
        self.template = self.template.replace(ROUTER_ROUTES, self.generateRoute())

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Router generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

