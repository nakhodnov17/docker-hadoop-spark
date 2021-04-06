# Docker multi-container environment with Hadoop, Spark and Hive

This is it: a Docker multi-container environment with Hadoop (HDFS), Spark and Hive. But without the large memory requirements of a Cloudera sandbox. (On my Windows 10 laptop (with WSL2) it seems to consume a mere 3 GB).

## Quick Start

First of all we need to build base images:
```shell
docker build -t maksim64/hadoop-base:3.2.1 ./hadoop/base
docker build -t maksim64/spark-base:3.2.1 ./spark/base
```

Then build all other images:
```shell
docker-compose build --no-cache --parallel
```

To deploy the HDFS-Spark-Hive cluster, run:
```shell
  docker-compose up
```

`docker-compose` creates a docker network that can be found by running `docker network list`, e.g. `docker-hadoop-spark-hive_default`.

Run `docker network inspect` on the network (e.g. `docker-hadoop-spark-hive_default`) to find the IP the hadoop interfaces are published on. Access these interfaces with the following URLs:

* `Datanode:` `localhost:9864`
* `Namenode:` `localhost:9870`
* `Nodemanager:` `localhost:8042`

  
* `History server`: `localhost:8188`
* `Resource manager`: `localhost:8088`


* `Spark master`: `localhost:8080`
* `Spark worker`: `localhost:8081`


* `Hive`: `localhost:10002`


You can add hosts mapping in your `hosts` file (`C:/Windows/System32/drivers/etc/hosts` on Windows, `/etc/hosts` on Linux) to resolve links correctly:
```text
localhost datanode
localhost namenode
localhost nodemanager
localhost historyserver
localhost resourcemanager
```

If your docker gateway configured to map a local subnet to other ip replace `localhost` with `<your-dockerhadoop_IP_address>`.

There some examples how to work on a server using:
* [Hadoop](hadoop/QUICKSTART.md)
* [Spark](spark/QUICKSTART.md)
* [Hive](hive/QUICKSTART.md)

## Configure Environment Variables

The configuration parameters can be specified in the hadoop.env file or as environmental variables for specific services (e.g. `namenode`, `datanode` etc.):
```
  CORE_CONF_fs_defaultFS=hdfs://namenode:8020
```

`CORE_CONF` corresponds to `core-site.xml`. 

So `CORE_CONF_fs_defaultFS=hdfs://namenode:8020` will be transformed into:
```xml
  <property><name>fs.defaultFS</name><value>hdfs://namenode:8020</value></property>
```
To define dash inside a configuration parameter, use triple underscore, such as `YARN_CONF_yarn_log___aggregation___enable=true` (`yarn-site.xml`):
```xml
  <property><name>yarn.log-aggregation-enable</name><value>true</value></property>
```

The available configurations are:
* `/etc/hadoop/core-site.xml` `CORE_CONF`
* `/etc/hadoop/hdfs-site.xml` `HDFS_CONF`
* `/etc/hadoop/yarn-site.xml` `YARN_CONF`
* `/etc/hadoop/httpfs-site.xml` `HTTPFS_CONF`
* `/etc/hadoop/kms-site.xml` `KMS_CONF`
* `/etc/hadoop/mapred-site.xml`  `MAPRED_CONF`

If you need to extend some other configuration file, refer to `hadoop/base/entrypoint.sh` bash script.
