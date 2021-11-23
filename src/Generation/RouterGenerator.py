from .Flags import ROUTER_MIDDLEWARE_IMPORTS, ROUTER_SANITIZER_IMPORTS, ROUTER_REQUEST_IMPORTS, ROUTER_CONTROLLER_IMPORTS, ROUTER_ROUTES, ROUTER_MIDDLEWARE_IMPORT_NAME
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import ROUTER_TEMPLATE_PATH, ROUTER_MIDDLEWARE_IMPORT_TEMPLATE_PATH

class RouterGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = toCodeCamelCase(self.catName)
        self.distFile = self.distPath + "/" + self.fileName + "Router.ts"
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, ROUTER_TEMPLATE_PATH)
        print('\nSetup Router generator\n', self.distFile, "\n")

    # def printFields(self):
    #     data = ""
    #     fields = self.json.navigate('fields')
    #     nbFields = len(fields.getContent())
    #     i = 0
    #     while i < nbFields:
    #         field = fields.navigate(str(i))
    #         data += readFile(MODEL_FIELD_TEMPLATE_PATH)
    #         data = data.replace(MODEL_FIELD_NAME, field.access('name'))
    #         data = data.replace(MODEL_FIELD_TYPE, field.access('modelType'))
    #         data += "\n"
    #         i += 1
    #     data += MODEL_FIELDS
    #     return data
    def importMiddlewares(self):
        data = ""
        list = self.json.access('middlewares')
        for elem in list:
            data += readFile(ROUTER_MIDDLEWARE_IMPORT_TEMPLATE_PATH)
            data+= "\n"
            data = data.replace(ROUTER_MIDDLEWARE_IMPORT_NAME, elem)
        data += ROUTER_MIDDLEWARE_IMPORTS
        return data


    def replaceFlags(self):
        self.template = self.template.replace(ROUTER_MIDDLEWARE_IMPORTS, self.importMiddlewares())
        # self.template = self.template.replace(ROUTER_SANITIZER_IMPORTS, self.fileName)
        # self.template = self.template.replace(ROUTER_REQUEST_IMPORTS, self.fileName)
        # self.template = self.template.replace(ROUTER_CONTROLLER_IMPORTS, self.fileName)
        # self.template = self.template.replace(ROUTER_ROUTES, self.fileName)

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Router generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

