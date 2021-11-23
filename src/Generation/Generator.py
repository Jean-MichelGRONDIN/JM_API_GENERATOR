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


# list les folders qu'il y à dans API/Routes/
# puis entre dans cheque folder et retien le nom
# puis lit chaque fichier et retien le nom du fichier
# $NOM_DU_FICHIER + $NOM_DU_DOSSIER + $COMPLEMENT (Action / Data / Request / Sanitizer)
# un fichier json par route
# dans le fichier json donner : la method, sanitizer, request, middlewares
# pas chercher si le model, le middleware, ... exist juste utilise les comme ci ils existait (ecrit les imports toi même)
# Comment je gère quand une data vient d'un middleware ? Genre auth avec le user_id ?


# Evolution ?: (Ne pas faire que du CRUD)
# Pouvoir les closes where des query ?
# ...

# validators
# DTOs
# Controllers
# Actions (check d'abord les where puis les actions dans l'ordre ou c'est arriver (input, update, ...))
