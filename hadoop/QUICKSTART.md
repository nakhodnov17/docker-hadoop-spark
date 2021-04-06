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

## Word count