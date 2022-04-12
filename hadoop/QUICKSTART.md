# Hadoop Quick Start

## HDFS

Copy breweries.csv to the namenode:
```shell
  docker cp examples/data/breweries.csv namenode:breweries.csv
```

Go to the bash shell on the namenode with that same Container ID of the namenode:
```shell
  docker exec -it namenode bash
```


Create a HDFS directory `/data/openbeer/breweries`:
```shell
  hdfs dfs -mkdir -p /data/openbeer/breweries
```

Copy breweries.csv to HDFS:
```shell
  hdfs dfs -put breweries.csv /data/openbeer/breweries/breweries.csv
```

See also: [python client for WebHDFS](../examples/WebHDFS/python_client.py).

## Word count with Hadoop Streaming

Move code and data to hadoop server
```shell
  docker cp examples/wordcount_streaming namenode:/
```

Go to the bash shell on the namenode with that same Container ID of the namenode:
```shell
  docker exec -it namenode bash
```

Start hadoop streaming script:
```shell
  cd wordcount_streaming
  sh run_hadoop.sh
```

Copy results from docker container:
```shell
  docker cp namenode:/wordcount_streaming/data/output examples/wordcount_streaming/data
```
