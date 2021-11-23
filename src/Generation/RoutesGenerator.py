from .RouterGenerator import RouterGenerator
from .DistPaths import ROUTER_DEST
from ..Tools.FilesHandler import getDirFolders, getDirFiles, readJsonFile
from ..Tools.JsonHandler import JsonHandler
from ..Tools.CleanningHandler import cleanRouterFile

class RoutesGenerator:
    def __init__(self, src, dist):
        print('\nSetup routes generator\n')
        self.confSrc = src
        self.generationDest = dist
        self.generatedRouters = []

    def generateRouter(self, catName, srcFilePath, srcFileName):
        destPath = self.generationDest + ROUTER_DEST
        jsonFile = JsonHandler(readJsonFile(srcFilePath))
        generator = RouterGenerator(catName, destPath, srcFileName, jsonFile)
        generator.run()
        distFilePath = generator.getDistFilePath()
        if distFilePath not in self.generatedRouters:
            self.generatedRouters.append(distFilePath)
        return

    def generateRoute(self, catName, srcFilePath, srcFileName):
        self.generateRouter(catName, srcFilePath, srcFileName)
        return


    def cleanRouters(self):
        for router in self.generatedRouters:
            cleanRouterFile(router)

    def cleanFiles(self):
        self.cleanRouters()

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

