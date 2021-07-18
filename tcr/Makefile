build:
	docker build -t tcr .

test:
	docker run -it -v $(PWD):/app tcr pytest --color=yes -p no:cacheprovider

commit:
	git add -A && git commit -m 'working'

revert:
	git reset --hard

branch_as_one_commit:
	git reset --soft master && git commit -m '(rename me!)' && git commit --amend