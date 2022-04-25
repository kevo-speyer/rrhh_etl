import logging
from pathlib import Path

class ETL:
    def __init__(self, **kargs):
        self.sql_dir = self.get_queries_dir()

    def get_queries_dir(self):
        sql_dir = Path(__file__).resolve().parents[1].joinpath('sqls')
        return sql_dir

    def run(self):
        logging.info(f'Running ETL from module {Path(__file__).stem}')
        query_file = 'agents_by_month.sql'
        with open(self.sql_dir.joinpath(query_file)) as f:
            sql = f.read() 
        1/0
