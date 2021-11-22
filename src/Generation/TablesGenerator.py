from .ModelGenerator import ModelGenerator
from .MigrationGenerator import MigrationGenerator
from .DistPaths import MODEL_DEST, MIGRATION_DEST
from ..Tools.FilesHandler import getDirFolders, getDirFiles, readJsonFile
from ..Tools.JsonHandler import JsonHandler
from ..Tools.CleanningHandler import cleanModelFile, cleanMigrationFile
from os.path import basename

class TablesGenerator:
    def __init__(self, src, dist):
        print('\nSetup tables generator\n')
        self.confSrc = src
        self.generationDest = dist

    def generateModel(self, filePath, fileName):
        destPath = self.generationDest + MODEL_DEST
        jsonFile = JsonHandler(readJsonFile(filePath))
        modelGenerator = ModelGenerator(destPath, fileName, jsonFile)
        modelGenerator.run()
        distFilePath = modelGenerator.getDistFilePath()
        cleanModelFile(distFilePath)
        return

    def generateMigration(self, migrationName, files):
        destPath = self.generationDest + MIGRATION_DEST
        jsonFiles = [[int(JsonHandler(readJsonFile(file)).access('order')), basename(file), JsonHandler(readJsonFile(file))] for file in files]
        orderList = sorted(jsonFiles, key=lambda elem: elem[0])
        migrationGenerator = MigrationGenerator(destPath, migrationName, orderList)
        migrationGenerator.run()
        distFilePath = migrationGenerator.getDistFilePath()
        cleanMigrationFile(distFilePath)
        return

    def generate(self):
        print('\nRun tables generator\n')
        foldersPath = self.confSrc + "/Tables"
        folders = getDirFolders(foldersPath)
        for migrationName in folders:
            migrationPath = foldersPath + "/" + migrationName
            files = getDirFiles(migrationPath)
            filesPaths = []
            for file in files:
                filePath = migrationPath + "/" + file
                filesPaths.append(filePath)
                self.generateModel(filePath, file)
            self.generateMigration(migrationName, filesPaths)
        return

    def run(self):
        self.generate()
        # clear files that are in the lists

