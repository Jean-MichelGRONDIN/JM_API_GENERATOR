from .TablesGenerator import TablesGenerator

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

        self.generateRoutes()
        # Clear flags
        # Clear les les virgules seul en fin de list (soir sur la même ligne sous sur plusieurs lignes)
        # except Exception as error:
        #     print("Failling to generate the API\n")
        #     print(error)
        #     return 1
        print("Generation Successful\n")
        return 0
        # try:
        #     #setup (copy template)
        #     #exec
        # except:
        #     #print error
        #     #delete generated folder (dist/)


# list les folders qu'il y à dans API/Routes/
# puis entre dans cheque folder et retien le nom
# puis lit chaque fichier et retien le nom du fichier
# $NOM_DU_FICHIER + $NOM_DU_DOSSIER + $COMPLEMENT (Action / Data / Request / Sanitizer)
# un fichier json par route
# dans le fichier json donner : la method, sanitizer, request, middlewares
# pas chercher si le model, le middleware, ... exist juste utilise les comme ci ils existait (ecrit les imports toi même)


# list chaques fichiers dans API/Tables/
# le nom des fichiers c'est du style action_likes
# génère les migration ? => Dire les fields, leur type (type model != type migration ? have to guess ?), si y'as des constraints, donner l'ordre dans lequel créer les migration (ptete repèrer des trucs avec les nom ? (has == liaison ?))
# créer le model en transformant le nom du fichier en KamelCase singulier : ActionLike ( utiliser une regex ^([a-Z]) to upper et tous les _([a-Z]) to upper sans le _ )


# Comment je gère quand une data vient d'un middleware ? Genre auth avec le user_id ?