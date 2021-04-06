current_branch := $(shell git rev-parse --abbrev-ref HEAD)
build:
	docker build -t hive-metastore-postgresql:$(current_branch) ./
