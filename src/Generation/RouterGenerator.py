from .Flags import MODEL_NAME, MODEL_FIELDS, MODEL_FIELD_NAME, MODEL_FIELD_TYPE
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import MODEL_TEMPLATE_PATH, MODEL_FIELD_TEMPLATE_PATH

class RouterGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = toCodeCamelCase(self.catName)
        self.distFile = self.distPath + "/" + self.fileName + "Router.ts"
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, MODEL_TEMPLATE_PATH)
        print('\nSetup Router generator\n', self.distFile, "\n")

    def printFields(self):
        data = ""
        fields = self.json.navigate('fields')
        nbFields = len(fields.getContent())
        i = 0
        while i < nbFields:
            field = fields.navigate(str(i))
            data += readFile(MODEL_FIELD_TEMPLATE_PATH)
            data = data.replace(MODEL_FIELD_NAME, field.access('name'))
            data = data.replace(MODEL_FIELD_TYPE, field.access('modelType'))
            data += "\n"
            i += 1
        data += MODEL_FIELDS
        return data


    def replaceFlags(self):
        self.template = self.template.replace(MODEL_NAME, self.fileName)
        self.template = self.template.replace(MODEL_FIELDS, self.printFields())

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun Router generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

