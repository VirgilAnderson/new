# Project: Logs analysis

The log analysis software was written with the express intention of analyzing the news data database provided for this project with an intention of extrapolating:

- Top 3 popular articles
- Most popular Authors
- Identify which days possessed an error ratio greater than 1%

The database in question is comprised of 3 separate tables: an author table, an article table and a log table.

Authors table

| Name | Bio | id |
| :------------- | :------------- | :------------- |
| text | text | var |

Article Table

| Author | Title | Slug | Lead | Body | Time | id |
| :------------- | :------------- | :------------- | :------------- | :------------- | :------------- | :------------- |
| text | text | text | text | text | datetime | var

Log

| path | IP | Method | status | time | id |
| :------------- | :------------- | :------------- | :------------- | :------------- | :------------- |
| text | var | text | text | datetime | var |

## Installation

In order to use this software, you must be running psql on your machine and you should be running a virtual machine that includes a postgreSQL database software.

Load your virtual machine with `vagrant up` and log in with the command `vagrant ssh`.

Once you're logged into your VM, you must download [newsdata.zip] (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip the file and extract newsdata.sql which should be loaded into your vagrant directory.

To load the data, `cd` into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

cd to the vagrant directory and  use the command `psql -d news -f newsdata.sql` to load the data into your psql database.

In order for the queries to function properly, you must create two views in your psql database; the daily queries view and the daily errors view.

To create these views, enter the following commands:

##### Daily queries view

```
CREATE  VIEW daily_que AS
SELECT CAST(time AS DATE), count(*) AS queries
FROM log GROUP BY CAST(time AS DATE)
ORDER BY time;
```

##### Daily errors views

```
CREATE VIEW daily_err AS
SELECT CAST(time AS DATE), count(*) AS errors
FROM log WHERE status!='200 OK'
GROUP BY CAST(time AS DATE)
ORDER BY CAST(time AS DATE);
```

### Usage
To use the software, `cd` to the newsdata directory and run the command: `python project_analysis.py`

The software will query your database and output the data requested.

#### License
The Log Analysis project is open source and it is free to be used or modified by anyone.
