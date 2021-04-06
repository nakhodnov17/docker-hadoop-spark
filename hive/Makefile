current_branch := $(shell git rev-parse --abbrev-ref HEAD)
build:
	docker build -t hive:$(current_branch) ./
