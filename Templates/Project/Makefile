include .env
export $(shell sed 's/=.*//' .env)

NAME = "default"
MODE = "development"

#TAKE THE DIRECTORY'S NAME
DIR=$(notdir $(shell pwd))
export DIR

# KEY=$(shell cat .env | grep API_KEY | sed "s/API_KEY=//g")
# CERT=$(shell cat .env | grep API_CERT | sed "s/API_CERT=//g")
# export KEY
# export CERT

# flag: -p, --project-name NAME     Specify an alternate project name
# flag: --build                     Build images before starting containers.
# flag: --remove-orphans            Remove containers for services not defined
# flag: --force-recreate            Recreate containers even if their configuration
# mkdir dist ; mv $(CERT) ./dist/ && mv $(KEY) ./dist/
api-dev-log:
	@echo -e "\n\t 🎧 🤖 \n\t💻 🔧 💉\n\t🚀 🛸 🛰\n"
	@docker-compose -p $(DIR) up --build --force-recreate --remove-orphans

api-dev:
	@echo -e "\n\t 🎧 🤖 \n\t💻 🔧 💉\n\t🚀 🛸 🛰\n"
	@docker-compose -p $(DIR) up --build --force-recreate --remove-orphans -d

api-dev-down:
	@echo -e "\n\t 🚨 🚧 ⭕️ 🛑 ⛔️\n\n"
	@docker-compose -p $(DIR) down --remove-orphans

api-dev-down-clean:
	@echo -e "\n\t 🚨 🚧 ⭕️ 🛑 ⛔️\n\n"
	@docker-compose -p $(DIR) down --remove-orphans --volumes

api-test:
	@echo -e "\n\t👷🏿 🧑🏼‍🔧 🥷🏼\n"
	@npm run coverage

api-backup:
	docker exec -t $(DIR)_database_1 pg_dump -a --inserts -U ${POSTGRES_USER} -p ${POSTGRES_PORT} | grep "INSERT" > db/backup/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql 

create-migrate:
	npx knex migrate:make -x ts $(NAME)

migrate:
	npx knex migrate:latest --env $(MODE)

migrate-rollback:
	npx knex migrate:rollback --env $(MODE)

create-seed:
	npx knex seed:make $(NAME)

seed:
	npx knex seed:run

.PHONY: api-dev api-dev-log api-backup create-migrate migrate seed create-seed api-dev-down api-dev-down-clean api-test
