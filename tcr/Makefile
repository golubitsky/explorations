build:
	docker build -t tcr .

test:
	docker run -it -v $(PWD):/app tcr pytest --color=yes -p no:cacheprovider

branch_as_one_commit:
	git reset --soft master && git commit -m 'my commit (rename me!)'