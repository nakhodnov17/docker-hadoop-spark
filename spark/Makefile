build_tag := 3.3.1
build:
	docker build -t maksim64/spark-base:$(build_tag) ./base
	docker build -t maksim64/spark-master:$(build_tag) ./master
	docker build -t maksim64/spark-worker:$(build_tag) ./worker
	docker build -t maksim64/spark-submit:$(build_tag) ./submit
	docker build -t maksim64/spark-java-template:$(build_tag) ./template/java
	docker build -t maksim64/spark-scala-template:$(build_tag) ./template/scala
	docker build -t maksim64/spark-python-template:$(build_tag) ./template/python
