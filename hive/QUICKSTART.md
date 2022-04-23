# Hive Quick Start 

Read `hadoop/QUICKSTART.md` before reading this.

Go to the command line of the Hive server:
```shell
  docker exec -it hive-server bash
```

Beeline is the command line interface with Hive. Let's connect to hiveserver2 now.

```shell
  beeline -u jdbc:hive2://127.0.0.1:10000 
```

Not a lot of databases here yet.
```shell
  show databases;
```
```text
>>: 
    +----------------+
    | database_name  |
    +----------------+
    | default        |
    +----------------+
    1 row selected (0.335 seconds)
```

Let's change that:
```sql
  create database openbeer;
  use openbeer;
```

Let's create a table:
```sql
CREATE EXTERNAL TABLE IF NOT EXISTS breweries(
    NUM INT,
    NAME CHAR(100),
    CITY CHAR(100),
    STATE CHAR(100),
    ID INT )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
location '/data/openbeer/breweries';
```

And have a little select statement going:
```sql
  select name from breweries limit 10;
```
```text
>>
    +----------------------------------------------------+
    |                        name                        |
    +----------------------------------------------------+
    | name                                               |
    | NorthGate Brewing                                  |
    | Against the Grain Brewery                          |
    | Jack's Abby Craft Lagers                           |
    | Mike Hess Brewing Company                          |
    | Fort Point Beer Company                            |
    | COAST Brewing Company                              |
    | Great Divide Brewing Company                       |
    | Tapistry Brewing                                   |
    | Big Lake Brewing                                   |
    +----------------------------------------------------+
    10 rows selected (0.113 seconds)
```

There you go: your private Hive server to play with.
