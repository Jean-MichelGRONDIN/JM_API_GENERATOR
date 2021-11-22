from .Flags import MIGRATION_UP, MIGRATION_DOWN, MIGRATION_TABLE_NAME
from ..Tools.FilesHandler import readFile, writeInFileByPath
from .TemplatesPaths import MIGRATION_TEMPLATE_PATH, MIGRATION_UP_TEMPLATE_PATH, MIGRATION_DOWN_TEMPLATE_PATH
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


    def printMigrationUp(self, tableName, json):
        data = ""
        data += readFile(MIGRATION_UP_TEMPLATE_PATH)
        data = data.replace(MIGRATION_TABLE_NAME, tableName)
        # for each field call print field function
        # paste createTableTemplate
        # send to flag createTableReplaceFlag and data = el ret
        data += "\n" + MIGRATION_UP
        return data

    def printMigrationDown(self, tableName):
        data = ""
        data += MIGRATION_DOWN + "\n"
        data += readFile(MIGRATION_DOWN_TEMPLATE_PATH)
        data = data.replace(MIGRATION_TABLE_NAME, tableName)
        return data


    def replaceFlags(self, file):
        tableName = file[1][:-5]
        json = file[2]
        self.template = self.template.replace(MIGRATION_UP, self.printMigrationUp(tableName, json))
        self.template = self.template.replace(MIGRATION_DOWN, self.printMigrationDown(tableName))

    def generate(self):
        for file in self.files:
            self.replaceFlags(file)

    def run(self):
        print('\nRun migration generator\n', self.distFile, "\n")
        self.generate()
        writeInFileByPath(self.distFile, self.template)

