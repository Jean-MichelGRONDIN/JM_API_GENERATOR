from .Flags import MIGRATION_UP, MIGRATION_DOWN, MIGRATION_TABLE_NAME, MIGRATION_FIELD_PLACEHOLDER, MIGRATION_REFERENCE_PLACEHOLDER, MIGRATION_FIELD_NAME, MIGRATION_FIELD_NAME, MIGRATION_FIELD_TYPE, MIGRATION_IS_NULLABLE, MIGRATION_DEFAULT, MIGRATION_DEFAULT_VALUE, MIGRATION_REFERENCE_FIELD_NAME, MIGRATION_REFERENCE_FIELD_TARGET
from ..Tools.FilesHandler import readFile, writeInFileByPath
from .TemplatesPaths import MIGRATION_TEMPLATE_PATH, MIGRATION_UP_TEMPLATE_PATH, MIGRATION_DOWN_TEMPLATE_PATH, MIGRATION_UP_TEMPLATE_FIELD_PATH, MIGRATION_UP_TEMPLATE_FIELD_NOT_NULLABLE_PATH, MIGRATION_UP_TEMPLATE_FIELD_DEFAULT_PATH, MIGRATION_UP_TEMPLATE_REFERENCE_PATH
from ..Tools.JsonHandler import JsonHandler
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


    def printMigrationFieldPlaceHolder(self, json):
        data = ""
        data += readFile(MIGRATION_UP_TEMPLATE_FIELD_PATH)
        data = data.replace(MIGRATION_FIELD_NAME, json.access('name'))
        data = data.replace(MIGRATION_FIELD_TYPE, json.access('type'))
        data += "\n\n" + MIGRATION_FIELD_PLACEHOLDER
        return data

    def printMigrationFieldIsNullable(self, json):
        data = ""
        if json.access('nullable') == False:
            data += readFile(MIGRATION_UP_TEMPLATE_FIELD_NOT_NULLABLE_PATH)
        return data

    def printMigrationFieldDefault(self, json):
        data = ""
        if json.access('default.exist'):
            data += readFile(MIGRATION_UP_TEMPLATE_FIELD_DEFAULT_PATH)
            data = data.replace(MIGRATION_DEFAULT_VALUE, json.access('default.value'))
        return data

    def printMigrationFieldReference(self, json):
        data = ""
        if json.access('references.isRef'):
            data += readFile(MIGRATION_UP_TEMPLATE_REFERENCE_PATH)
            data = data.replace(MIGRATION_REFERENCE_FIELD_NAME, json.access('name'))
            data = data.replace(MIGRATION_REFERENCE_FIELD_TARGET, json.access('references.refTo'))
        return data

    def printMigrationUp(self, tableName, json):
        data = ""
        data += readFile(MIGRATION_UP_TEMPLATE_PATH)
        data = data.replace(MIGRATION_TABLE_NAME, tableName)

        for field in json.access('fields'):
            jsonField = JsonHandler(field)
            data = data.replace(MIGRATION_FIELD_PLACEHOLDER, self.printMigrationFieldPlaceHolder(jsonField))
            data = data.replace(MIGRATION_IS_NULLABLE, self.printMigrationFieldIsNullable(jsonField))
            data = data.replace(MIGRATION_DEFAULT, self.printMigrationFieldDefault(jsonField))
            data = data.replace(MIGRATION_REFERENCE_PLACEHOLDER, self.printMigrationFieldReference(jsonField))
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

