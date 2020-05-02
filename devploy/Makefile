DOCKER_COMPOSE=docker-compose -f docker-compose.yml
DOCKER_COMPOSE_RUN=$(DOCKER_COMPOSE) run --rm

build:
	$(DOCKER_COMPOSE) build

up: build
	$(DOCKER_COMPOSE) up

run: build
	$(DOCKER_COMPOSE_RUN) $(service) $(cmd)

test: build
	$(DOCKER_COMPOSE_RUN) $(service) pytest -f --color=yes -p no:cacheprovider

down:
	$(DOCKER_COMPOSE) down

clean:
	$(DOCKER_COMPOSE) down -v

