Following https://www.udemy.com/course/learn-clickhouse.

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

## Clickhouse SQL

### DDL (Data Definition Language)

CREATE [can be used](https://clickhouse.com/docs/en/sql-reference/statements/create) to create databases, users, roles, etc.

RENAME can be used for databases, tables, and [dictionaries](https://clickhouse.com/docs/en/sql-reference/dictionaries).

TRUNCATE, DROP

### DQL (Query)

### DML (Manipulation)

INSERT, ALTER, UPDATE, DELETE

Mutations [are costly](https://clickhouse.com/docs/en/optimize/avoid-mutations).

UPDATE is used with ALTER:

> The ALTER TABLE prefix makes this syntax different from most other systems supporting SQL. It is intended to signify that unlike similar queries in OLTP databases this is a heavy operation not designed for frequent use.

`DELETE` without `ALTER` is a [lightweight delete](https://clickhouse.com/docs/en/guides/developer/lightweight-delete).

### DCL (Control)

GRANT, REVOKE

### Views

Views are based on another table and defined with a SQL query.

Materialized views

- can use a different engine from the underlying table.
- only reflect INSERT operations; not UPDATE and DELETE.

### Joins

Joins use a hash merge by default.

- Inner
  - only records matching in both tables
- Left
  - all records from left table, including matching records from right table
- Right
  - all records from right table, including matching records from left table
- Full
  - all records from both tables are returned, with nulls where there are no matching records
- Cross

### Operators

Essentially same as Postgres.
Each operator has an equivalent function, e.g., "a + b" is equivalent to plus(a, b).

- Mathematical
  - +, -, \*, /, %
- Comparison
  - ==, != or <>, <, >, <=, >=, (not) like, a (not) between b and c
- Logical
  - NOT, AND, OR
- Null
  - IS (NOT) NULL

### Data Types

- Numeric
  - integer (8-bit to 256-bit)
    - signed
    - unsigned
  - float (32- and 64-bit)
    - rounding errors
  - decimal (32- through 256-bit)
    - stores fractions with fixed decimal point
    - up to: precision 39-75, scale 0-75
    - when dividing, least significant digits are discarded (not rounded)
  - infinity and nan
    - infinity represented by `-1/0` and `1/0`
    - nan represented by `0/0`
  - boolean
- String
  - not automatically encoded; [some built-in functions assume UTF-8](https://clickhouse.com/docs/en/sql-reference/data-types/string#encodings)
  - string (like VARCHAR)
    - stored as bytes
    - no fixed length
  - fixed string (like CHAR)
    - fixed length (in bytes)
    - if length < max length
      - null characters appended
    - if length > max length
      - exception
- Date
  - Date – based on UNIX epoch, two bytes
  - Date32 — 32-bit integer
  - no support for time zones
- Datetime
  - DateTime — supports second precision
  - DateTime64 — supports subsecond precision
  - supports IANA time zones
- Array
- Tuple
- Nested
- Enum
- Low cardinality
- Geo
