from .FilesHandler import readJsonFile

class JsonHandler:
    def __init__(self, json):
        self.content = json

    def getContent(self):
        return self.content.copy()

    def accessInJson(self, content, deeps):
        key = deeps[0]
        # print(deeps)
        # print(key)
        # print(content)
        # print("\n")
        if key.isnumeric():
            key = int(key)
        content = content[key]
        if len(deeps) > 1:
            return self.accessInJson(content, (deeps[1:]))
        return content

    def access(self, varPath):
        deeps = varPath.split('.')
        return self.accessInJson(self.getContent(), deeps)

    def navigate(self, varPath):
        return JsonHandler(self.access(varPath))

