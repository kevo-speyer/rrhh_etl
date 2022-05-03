import logging
import pandas as pd
from pathlib import Path
from rrhh_etl.utils import db_connections

class ETL:
    def __init__(self, **kwargs):
        logging.info(f'Initializing ETL from module {Path(__file__).stem}')
        self.engine_source = db_connections.get_engine(kwargs['db_source'], dbms='postgresql')
        self.engine_destination = db_connections.get_engine(kwargs['db_destination'], dbms='postgresql')

    def backfill(self, from_date=None):
        logging.info(f'Running backfill ETL from module {Path(__file__).stem}')
        # Extract and Transform
        query_file = 'backfill.sql'
        with open(self.get_query_path(query_file)) as f:
            query = f.read()
        with self.engine_source.connect() as con:
            df_backfill = pd.read_sql(query, con=con)
        logging.info(f'Results fetched from backfill ETL from module {Path(__file__).stem}')
        # Load
        dest_table = 'daily_inscriptions'
        with self.engine_destination.connect() as con:
            df_backfill.to_sql(dest_table, con=con, if_exists='replace')
        logging.info(f'Backfill into table {dest_table} done from module {Path(__file__).stem}')
        
    def get_query_path(self, query_file):
        sql_dir = Path(__file__).resolve().parents[1].joinpath('sqls')
        sql_path = sql_dir.joinpath(query_file)
        return sql_path

    def update(self):
        logging.info(f'Running update from module {Path(__file__).stem}')

    def run(self, action):
        run_action = getattr(self, action)
        run_action()
 
