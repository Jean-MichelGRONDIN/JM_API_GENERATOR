from .Flags import MODEL_NAME, MODEL_FIELDS, MODEL_FIELD_NAME, MODEL_FIELD_TYPE
from ..Tools.FilesHandler import readFile, writeInFileByPath
from ..Tools.CaseHandler import toTitleCamelCase
from .TemplatesPaths import MODEL_TEMPLATE_PATH, MODEL_FIELD_TEMPLATE_PATH

def getModelFileNameFromFileName(fileName):
    return toTitleCamelCase(fileName[:-5]) + ".ts"

def getModelFileNameFromCatName(catName):
    return toTitleCamelCase(catName) + ".ts"

class ModelGenerator:
    def __init__(self, distPath, fileName, jsonFile):
        self.distPath = distPath
        self.fileName = getModelFileNameFromFileName(fileName)
        self.distFile = self.distPath + "/" + self.fileName
        self.json = jsonFile
        self.template = readFile(MODEL_TEMPLATE_PATH)
        print('\nSetup model generator\n', self.distFile, "\n")

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
        self.template = self.template.replace(MODEL_NAME, self.fileName[:-3])
        self.template = self.template.replace(MODEL_FIELDS, self.printFields())

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        print('\nRun model generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

