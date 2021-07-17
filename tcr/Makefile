build:
	docker build -t tcr .

test:
	docker run -it -v $(PWD):/app tcr pytest --color=yes -p no:cacheprovider
