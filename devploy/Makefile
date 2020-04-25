DOCKER_COMPOSE=docker-compose -f docker-compose.yml

build:
	$(DOCKER_COMPOSE) build

up: build
	$(DOCKER_COMPOSE) up

test: build
	$(DOCKER_COMPOSE) run --rm $(service) pytest -f --color=yes -p no:cacheprovider

down:
	$(DOCKER_COMPOSE) down

clean:
	$(DOCKER_COMPOSE) down -v

