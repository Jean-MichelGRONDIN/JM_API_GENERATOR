from .TablesGenerator import TablesGenerator
from .RoutesGenerator import RoutesGenerator

class Generator:
    def __init__(self, confSrc):
        print('Building generator\n')
        if confSrc[-1:] == "/":
            self.confSrc = confSrc[:-1]
        else:
            self.confSrc = confSrc
        self.generationDest = "./dist/"

    def generateRoutes(self):
        return

    def run(self):
        print('Running generator\n')
        # try:
        tablesGenerator = TablesGenerator(self.confSrc, self.generationDest)
        tablesGenerator.run()

        tablesGenerator = RoutesGenerator(self.confSrc, self.generationDest)
        tablesGenerator.run()
        #     # Clear les les virgules seul en fin de list (soir sur la même ligne sous sur plusieurs lignes)
        #     # replace every \t par 4 espaces
        # except Exception as error:
        #     print("Failling to generate the API\n")
        #     print(error)
        #     return 1
        print("Generation Successful\n")
        return 0


# DTO (donner la possibilité de mettre un rawFile à la place d'un raw et donc changer de template pour la value et juste mettre le contenu du file, le nom du file serai "filejsonName+dataName+.ts" action.user_id.ts)
# Ajouter un orderby dans les fichier conf ( au niveau de la route orderby: has, rule)
# Ajouter un rawQuery dans les fichiers conf (rawQuery: has, query), du coup ça change le template utiliser pour l'action


