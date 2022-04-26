import logging
from pathlib import Path
from utils import db_connections

class ETL:
    def __init__(self, **kwargs):
        engine = db_connections.get_engine(kwargs['db_source'])
        print(engine)
        #print(kwargs['db_destination'])
        self.sql_dir = self.get_queries_dir()
        # init db connections
        # query db
        # transform + save intermediate state
        # load

    def get_queries_dir(self):
        sql_dir = Path(__file__).resolve().parents[1].joinpath('sqls')
        return sql_dir

    def run(self):
        logging.info(f'Running ETL from module {Path(__file__).stem}')
        query_file = 'agents_by_month.sql'
        with open(self.sql_dir.joinpath(query_file)) as f:
            sql = f.read()
 
