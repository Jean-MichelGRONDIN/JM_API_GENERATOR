from .RouterGenerator import RouterGenerator
from .DistPaths import ROUTER_DEST, SANITIZER_DEST, VALIDATOR_DEST, DTO_DEST, CONTROLLER_DEST
from ..Tools.FilesHandler import getDirFolders, getDirFiles, readJsonFile
from ..Tools.JsonHandler import JsonHandler
from ..Tools.CleanningHandler import cleanRouterFile, cleanSanitizerFile, cleanValidatorFile, cleanDTOFile, cleanControllerFile
from .SanitizerGenerator import hasSanitizer, SanitizerGenerator
from .ValidatorGenerator import hasValidator, ValidatorGenerator
from .DTOGenerator import DTOGenerator
from .ControllerGenerator import ControllerGenerator

class RoutesGenerator:
    def __init__(self, src, dist):
        print('\nSetup routes generator\n')
        self.confSrc = src
        self.generationDest = dist
        self.generatedRouters = []
        self.generatedSanitizers = []
        self.generatedValidators = []
        self.generatedControllers = []
        self.generatedDTOs = []
        self.generatedActions = []

    def generateRouter(self, catName, srcFilePath, srcFileName):
        destPath = self.generationDest + ROUTER_DEST
        jsonFile = JsonHandler(readJsonFile(srcFilePath))
        generator = RouterGenerator(catName, destPath, srcFileName, jsonFile)
        generator.run()
        distFilePath = generator.getDistFilePath()
        if distFilePath not in self.generatedRouters:
            self.generatedRouters.append(distFilePath)
        return

    def generateSanitizer(self, catName, srcFilePath, srcFileName):
        destPath = self.generationDest + SANITIZER_DEST
        jsonFile = JsonHandler(readJsonFile(srcFilePath))
        if hasSanitizer(jsonFile):
            generator = SanitizerGenerator(catName, destPath, srcFileName, jsonFile)
            generator.run()
            distFilePath = generator.getDistFilePath()
            if distFilePath not in self.generatedSanitizers:
                self.generatedSanitizers.append(distFilePath)
        return

    def generateValidator(self, catName, srcFilePath, srcFileName):
        destPath = self.generationDest + VALIDATOR_DEST
        jsonFile = JsonHandler(readJsonFile(srcFilePath))
        if hasValidator(jsonFile):
            generator = ValidatorGenerator(catName, destPath, srcFileName, jsonFile)
            generator.run()
            distFilePath = generator.getDistFilePath()
            if distFilePath not in self.generatedSanitizers:
                self.generatedSanitizers.append(distFilePath)
        return

    def generateDTO(self, catName, srcFilePath, srcFileName):
        destPath = self.generationDest + DTO_DEST
        jsonFile = JsonHandler(readJsonFile(srcFilePath))
        if hasValidator(jsonFile):
            generator = DTOGenerator(catName, destPath, srcFileName, jsonFile)
            generator.run()
            distFilePath = generator.getDistFilePath()
            if distFilePath not in self.generatedDTOs:
                self.generatedDTOs.append(distFilePath)
        return

    def generateController(self, catName, srcFilePath, srcFileName):
        destPath = self.generationDest + CONTROLLER_DEST
        jsonFile = JsonHandler(readJsonFile(srcFilePath))
        generator = ControllerGenerator(catName, destPath, srcFileName, jsonFile)
        generator.run()
        distFilePath = generator.getDistFilePath()
        if distFilePath not in self.generatedControllers:
            self.generatedControllers.append(distFilePath)
        return

    def generateRoute(self, catName, srcFilePath, srcFileName):
        self.generateRouter(catName, srcFilePath, srcFileName)
        self.generateSanitizer(catName, srcFilePath, srcFileName)
        self.generateValidator(catName, srcFilePath, srcFileName)
        self.generateDTO(catName, srcFilePath, srcFileName)
        self.generateController(catName, srcFilePath, srcFileName)
        return


    def cleanFilesListWithRule(self, list, func):
        for file in list:
            func(file)

    def cleanFiles(self):
        self.cleanFilesListWithRule(self.generatedRouters, cleanRouterFile)
        self.cleanFilesListWithRule(self.generatedSanitizers, cleanSanitizerFile)
        self.cleanFilesListWithRule(self.generatedValidators, cleanValidatorFile)
        self.cleanFilesListWithRule(self.generatedDTOs, cleanDTOFile)
        self.cleanFilesListWithRule(self.generatedControllers, cleanControllerFile)


    def generate(self):
        print('\nRun routes generator\n')
        foldersPath = self.confSrc + "/Routes"
        folders = getDirFolders(foldersPath)
        for catName in folders:
            catPath = foldersPath + "/" + catName
            files = getDirFiles(catPath)
            for file in files:
                filePath = catPath + "/" + file
                self.generateRoute(catName, filePath, file)
        self.cleanFiles()
        return

    def run(self):
        self.generate()

