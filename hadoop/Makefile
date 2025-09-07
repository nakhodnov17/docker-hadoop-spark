DOCKER_NETWORK = docker-hadoop_default
ENV_FILE = hadoop.env
build_tag := 3.4.2
build:
	docker build -t maksim64/hadoop-base:$(build_tag) ./base
	docker build -t maksim64/hadoop-datanode:$(build_tag) ./datanode
	docker build -t maksim64/hadoop-namenode:$(build_tag) ./namenode
	docker build -t maksim64/hadoop-nodemanager:$(build_tag) ./nodemanager
	docker build -t maksim64/hadoop-historyserver:$(build_tag) ./historyserver
	docker build -t maksim64/hadoop-resourcemanager:$(build_tag) ./resourcemanager

#wordcount:
#	docker build -t hadoop-wordcount ./submit
#	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} maksim64/hadoop-base:$(build_tag) hdfs dfs -mkdir -p /input/
#	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} maksim64/hadoop-base:$(build_tag) hdfs dfs -copyFromLocal -f /opt/hadoop-3.4.2/README.txt /input/
#	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} hadoop-wordcount
#	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} maksim64/hadoop-base:$(build_tag) hdfs dfs -cat /output/*
#	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} maksim64/hadoop-base:$(build_tag) hdfs dfs -rm -r /output
#	docker run --network ${DOCKER_NETWORK} --env-file ${ENV_FILE} maksim64/hadoop-base:$(build_tag) hdfs dfs -rm -r /input
