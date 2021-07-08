IMAGE_NAME = another-python-chess:develop
export IMAGE_NAME # for docker-compose.yml

build:
	docker build -t $(IMAGE_NAME) .

server: build
	docker-compose up

test: build
	docker-compose run --rm develop pytest -f --color=yes -p no:cacheprovider

feedback: build
	docker-compose run --rm develop watch --color -n 1 python3 src/game.py