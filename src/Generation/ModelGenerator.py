from ..Tools.FilesHandler import readFile, writeInFileByPath
from ..Tools.CaseHandler import toTitleCamelCase
from .TemplatesPaths import MODEL_TEMPLATE_PATH

class ModelGenerator:
    def __init__(self, distPath, fileName, jsonFile):
        print('Building generator\n')
        self.distPath = distPath
        self.fileName = fileName
        self.json = jsonFile.copy()
        self.template = readFile(MODEL_TEMPLATE_PATH)

    def run(self):
        writeInFileByPath(self.distPath + "/" + toTitleCamelCase(self.fileName[:-5]) + ".ts", self.template)

