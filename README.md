
# codetest example
Example of reading out a public soap server and put data in localhosted sql database.


## startup
start `start_mysql.sh` to start mysql server. Credentials are: 
```
[sql]
user=pieter
password=w8woord
database=codetest
host=localhost
```

Run `poetry install` from `codetest/.` to install dependencies.

Run package by `poetry run python codetest/main.py` from `codetest/.`
*there was a weird bug in running it as a package.

## usage

```
options:
  -h, --help            show this help message and exit
  --config CONFIG       location of config file
  --dataset-definitions-dir DATASET_DEFINITIONS_DIR
                        directory where the dataset definitions reside.
  --country-info-instr-file COUNTRY_INFO_INSTR_FILE
                        location of country info instruction file
  --show_data           If given shows data in countries table, skips rest.
```
