# README

This project is meant to perform Extrat Transform and Load (ETL) operations.

## QuickStart:

### Install the rrhh_etls project
`$ ./install.sh`

### Activate created virtual env
`$ source venv/bin/activate`

### Run an ETL 
`$ rrhh_etl altas_bajas`

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
