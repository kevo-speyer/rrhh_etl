# README

This project is a simple package to develop your Extract Transform and Load (ETL) operations.

## QuickStart:

### Install the rrhh_etls project
`$ make install`

### Activate created virtual env
`$ source venv/bin/activate`

### Run an ETL 
`$ rrhh_etl daily_inscriptions`

### To see mannual
`$ rrhh_etl -h`

## Package Structure:

### Entrypoint 
    rrhh_etl/app.py

### Config
    rrhh_etl/config.yaml

### Pipelines
    rrhh_etl/etls/

### Queries
    rrhh_etl/sqls/

### Helpers
    rrhh_etl/utils/
