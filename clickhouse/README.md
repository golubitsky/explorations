## Installation

Spin up a Clickhouse server:

```sh
docker-compose up
```

In a separate terminal, run the [client](https://clickhouse.com/docs/en/interfaces/cli) inside the same docker container:

```sh
docker exec -it clickhouse-server clickhouse-client
```

Access the web UI here: http://localhost:8123/play.

You can also use [DBeaver](https://dbeaver.io/download/).

## Sample Data

This file is about 685.61 MB and has ~40 M rows of data.

```sh
wget http://datasets.clickhouse.com/cell_towers.csv.xz
```

Decompress the file (resulting size is 4.7 GB):

```sh
xz -d cell_towers.csv.xz
```

Copy the file into the Docker container:

```sh
docker cp cell_towers.csv clickhouse-server:/cell_towers.csv
```

Create the database:

```sql
CREATE DATABASE sample_dataset;
```

Create the table:

```sql
CREATE TABLE sample_dataset.cell_towers (
    `radio` Enum8('' = 0, 'CDMA' = 1, 'GSM' = 2, 'LTE' = 3, 'NR' = 4, 'UMTS' = 5),
    `mcc` UInt16,
    `net` UInt16,
    `area` UInt16,
    `cell` UInt64,
    `unit` Int16,
    `lon` Float64,
    `lat` Float64,
    `range` UInt32,
    `samples` UInt32,
    `changeable` UInt8,
    `created` DateTime,
    `updated` DateTime,
    `averageSignal` UInt8
) ENGINE = MergeTree()
ORDER BY (radio, mcc, net, area, cell);
```

Insert the data into the table:

```sh
$ docker exec -it clickhouse-server bash
root@86f097eb6037:/# clickhouse-client --query "INSERT INTO sample_dataset.cell_towers FORMAT CSVWithNames" < /cell_towers.csv
```

Clickhouse can import data in [a variety of formats](https://clickhouse.com/docs/en/interfaces/formats).

If you see no errors, verify that it worked:

```sql
SELECT count(*) FROM sample_dataset.cell_towers;
SELECT * FROM sample_dataset.cell_towers LIMIT 5;
```

