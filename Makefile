
help:
	@echo "up:\t\t\t container up"
	@echo "down:\t\t\t container down"
	@echo "test:\t\t\t start tests"
	@echo "makemigrations:\t\t makemigrations"
	@echo "migrate:\t\t migrate"

.PHONY: up
up:
	@docker-compose up -d

.PHONY:
down: up
	@docker-compose down

.PHONY:
test: up
	@docker-compose exec web python manage.py test

.PHONY:
makemigrations: up
	@docker-compose exec web python manage.py makemigrations

.PHONY:
migrate: up
	@docker-compose exec web python manage.py migrate
