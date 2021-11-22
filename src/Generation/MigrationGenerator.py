from .Flags import MODEL_NAME, MODEL_FIELDS
from ..Tools.FilesHandler import readFile, writeInFileByPath
from .TemplatesPaths import MIGRATION_TEMPLATE_PATH
from datetime import datetime

class MigrationGenerator:
    def __init__(self, distPath, fileName, tableFiles):
        self.distPath = distPath
        now = datetime.now()
        self.fileName = now.strftime("%Y%m%d_create_") + fileName + "_tables.ts"
        self.distFile = self.distPath + "/" + self.fileName + ".ts"
        self.files = tableFiles
        # self.revList = sorted(tableFiles, key=lambda elem: elem[0], reverse=True)
        self.template = readFile(MIGRATION_TEMPLATE_PATH)
        print('\nSetup migration generator\n', self.distFile, "\n")

    # def printFields(self):
    #     data = ""
    #     fields = self.json.navigate('fields')
    #     nbFields = len(fields.getContent())
    #     i = 0
    #     while i < nbFields:
    #         field = fields.navigate(str(i))
    #         data += "\t"
    #         data += field.access('name')
    #         data += ": "
    #         data += field.access('modelType')
    #         data += ",\n"
    #         i += 1
    #     data += MODEL_FIELDS
    #     return data


    # def replaceFlags(self):
    #     self.template = self.template.replace(MODEL_NAME, self.fileName)
    #     self.template = self.template.replace(MODEL_FIELDS, self.printFields())

    def run(self):
        print('\nRun migration generator\n', self.distFile, "\n")
        # self.replaceFlags()
        writeInFileByPath(self.distFile, self.template)

