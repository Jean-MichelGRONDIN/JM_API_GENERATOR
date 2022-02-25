from ..Tools.JsonHandler import JsonHandler
from ..Tools.FilesHandler import readFile, writeInFileByPath, genrateFileFromTemplateAndRead
from ..Tools.CaseHandler import toCodeCamelCase
from .TemplatesPaths import DTO_TEMPLATE_PATH, DTO_DUO_TEMPLATE_PATH, DTO_STRUC_FIELD_TEMPLATE_PATH, DTO_FUNC_RETRIEVES_TEMPLATE_PATH, DTO_ASYNC_TEMPLATE_PATH
from .TemplatesPaths import DTO_FUNC_RETRIEVE_FROM_BODY_TEMPLATE_PATH, DTO_FUNC_RETRIEVE_FROM_PARAMS_TEMPLATE_PATH, DTO_RAW_IMPORT_TEMPLATE_PATH
from .Flags import DTO_RAW_IMPORT_PLACEHOLDER, DTO_PLACEHOLDER, DTO_STRUC_NAME, DTO_FUNC_NAME
from .Flags import DTO_STRUC_FIELDS, DTO_FUNC_RETRIEVES, DTO_STRUC_FIELD_NAME, DTO_STRUC_FIELD_TYPE
from .Flags import DTO_FUNC_RETRIEVE_NAME, DTO_FUNC_RETRIEVE_VALUE, DTO_RAW_IMPORT_VALUE, DTO_ASYNC_PLACEHOLDER
from .Flags import DTO_FUNC_RETRIEVE_VALUE_FROM_BODY_NAME, DTO_FUNC_RETRIEVE_VALUE_FROM_PARAMS_NAME

def getDTOFileName(catName):
    return toCodeCamelCase(catName + "Data.ts")

def getDTOStrucName(catName, actionName):
    return toCodeCamelCase(catName + "_" + actionName + "Data")

def getDTOFuncName(catName, actionName):
    return getDTOStrucName(catName, actionName) + "FromRequest"

def doesNeedDTO(jsonFile):
    if len(jsonFile.access('data')) > 0:
        return True
    return False

class DTOGenerator:
    def __init__(self, catName, distPath, srcFileName, jsonFile):
        self.catName = catName
        self.distPath = distPath
        self.srcFileName = srcFileName
        self.fileName = getDTOFileName(self.catName)
        self.distFile = self.distPath + self.fileName
        self.json = jsonFile
        self.template = genrateFileFromTemplateAndRead(self.distFile, DTO_TEMPLATE_PATH)
        print('\nSetup DTO generator\n', self.distFile, "\n")


    def generateDTOStrucFields(self, ret, elemJson):
        ret = ret.replace(DTO_STRUC_FIELDS, readFile(DTO_STRUC_FIELD_TEMPLATE_PATH))
        ret = ret.replace(DTO_STRUC_FIELD_NAME, elemJson.access('name'))
        ret = ret.replace(DTO_STRUC_FIELD_TYPE, elemJson.access('type'))
        return ret

    def getDTORetrieveValueFromBody(self, elemJson):
        ret = ""
        ret = readFile(DTO_FUNC_RETRIEVE_FROM_BODY_TEMPLATE_PATH)
        ret = ret.replace(DTO_FUNC_RETRIEVE_VALUE_FROM_BODY_NAME, elemJson.access('name'))
        return ret

    def getDTORetrieveValueFromParams(self, elemJson):
        ret = ""
        ret = readFile(DTO_FUNC_RETRIEVE_FROM_PARAMS_TEMPLATE_PATH)
        ret = ret.replace(DTO_FUNC_RETRIEVE_VALUE_FROM_PARAMS_NAME, elemJson.access('name'))
        return ret

    def getDTORetrieveValueFromRaw(self, elemJson):
        if elemJson.access('get.rawImport') not in self.template:
            self.template = self.template.replace(DTO_RAW_IMPORT_PLACEHOLDER, readFile(DTO_RAW_IMPORT_TEMPLATE_PATH))
            self.template = self.template.replace(DTO_RAW_IMPORT_VALUE, elemJson.access('get.rawImport'))
        return elemJson.access('get.rawValue')

    def getDTORetrieveValue(self, elemJson):
        dataFrom = elemJson.access('get.from')
        types = [["body", self.getDTORetrieveValueFromBody], ["params", self.getDTORetrieveValueFromParams], ["rawLine", self.getDTORetrieveValueFromRaw]]
        for type in types:
            if dataFrom == type[0]:
                return type[1](elemJson)
        return self.getDTORetrieveValueFromBody(elemJson)

    def generateDTOFuncRetrieves(self, ret, elemJson):
        if elemJson.access('get.from') == "rawBloc":
            self.template = self.template.replace(DTO_RAW_IMPORT_PLACEHOLDER, readFile(DTO_RAW_IMPORT_TEMPLATE_PATH))
            self.template = self.template.replace(DTO_RAW_IMPORT_VALUE, elemJson.access('get.rawImport'))
            ret = ret.replace(DTO_FUNC_RETRIEVES, readFile(self.srcFileName[:-5] + "_" + elemJson.access('name') + ".ts"))
            ret += "\n" + DTO_FUNC_RETRIEVES
        else:
            ret = ret.replace(DTO_FUNC_RETRIEVES, readFile(DTO_FUNC_RETRIEVES_TEMPLATE_PATH))
            ret = ret.replace(DTO_FUNC_RETRIEVE_NAME, elemJson.access('name'))
            ret = ret.replace(DTO_FUNC_RETRIEVE_VALUE, self.getDTORetrieveValue(elemJson))
        return ret

    def generateDTO(self):
        ret = ""
        ret += readFile(DTO_DUO_TEMPLATE_PATH)
        ret = ret.replace(DTO_STRUC_NAME, getDTOStrucName(self.catName, self.srcFileName[:-5]))
        ret = ret.replace(DTO_FUNC_NAME, getDTOFuncName(self.catName, self.srcFileName[:-5]))
        data = self.json.access('data')
        for elem in data:
            elemJson = JsonHandler(elem)
            ret = self.generateDTOStrucFields(ret, elemJson)
            ret = self.generateDTOFuncRetrieves(ret, elemJson)
        ret = ret.replace(DTO_STRUC_FIELDS, "")
        ret = ret.replace(DTO_FUNC_RETRIEVES, "")
        return ret

    def replaceFlags(self):
        generatedDto = self.generateDTO()
        if " await " in generatedDto:
            generatedDto.replace(DTO_ASYNC_PLACEHOLDER, readFile(DTO_ASYNC_TEMPLATE_PATH))
        self.template = self.template.replace(DTO_PLACEHOLDER, generatedDto)
        print("Aprés generation du DTO: ", self.template)

    def getDistFilePath(self):
        return self.distFile

    def run(self):
        if doesNeedDTO(self.json):
            print('\nRun DTO generator\n', self.distFile, "\n")
            self.replaceFlags()
            writeInFileByPath(self.distFile, self.template)
        else:
            print('\nNo DTO to generate\n', self.distFile, "\n")
