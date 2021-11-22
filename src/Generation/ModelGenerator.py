from .Flags import MODEL_NAME, MODEL_FIELDS
from ..Tools.FilesHandler import readFile, writeInFileByPath
from ..Tools.CaseHandler import toTitleCamelCase
from .TemplatesPaths import MODEL_TEMPLATE_PATH

class ModelGenerator:
    def __init__(self, distPath, fileName, jsonFile):
        self.distPath = distPath
        self.fileName = toTitleCamelCase(fileName[:-5])
        self.distFile = self.distPath + "/" + self.fileName + ".ts"
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
            data += "\t"
            data += field.access('name')
            data += ": "
            data += field.access('modelType')
            data += ",\n"
            i += 1
        data += MODEL_FIELDS
        return data


    def replaceFlags(self):
        self.template = self.template.replace(MODEL_NAME, self.fileName)
        self.template = self.template.replace(MODEL_FIELDS, self.printFields())

    def run(self):
        print('\nRun model generator\n', self.distFile, "\n")
        self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

