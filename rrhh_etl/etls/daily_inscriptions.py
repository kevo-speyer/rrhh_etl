import logging
import pandas as pd
from pathlib import Path
from jinja2 import Template
from rrhh_etl.utils import db_connections


class ETL:
    def __init__(self, **kwargs):
        logging.info(f"Initializing ETL from module {Path(__file__).stem}")
        self.engine_source = db_connections.get_engine(
            kwargs["db_source"], dbms="postgresql"
        )
        self.engine_destination = db_connections.get_engine(
            kwargs["db_destination"], dbms="postgresql"
        )

    def backfill(self, start=None, to=None):
        logging.info(f"Running backfill ETL from module {Path(__file__).stem}")
        dest_table = "daily_inscriptions"

        # Render query with parameters
        query_file = "backfill.sql"
        with open(self.get_query_path(query_file)) as f:
            template = Template(f.read())
        query = template.render({"from_year": start, "to_date": to})

        # Extract and Transform
        with self.engine_source.connect() as con:
            df_backfill = pd.read_sql(query, con=con)
        logging.info("Results fetched!")

        # Load
        with self.engine_destination.connect() as con:
            df_backfill.to_sql(dest_table, con=con, if_exists="replace")

        logging.info(f"Backfill into table {dest_table} done!")

    def get_query_path(self, query_file):
        sql_dir = Path(__file__).resolve().parents[1].joinpath("sqls")
        sql_path = sql_dir.joinpath(query_file)
        return sql_path

    def update(self, **kwargs):
        # NOT YET IMPLEMENTED
        logging.info("Update method not yet implemented")

    def run(self, action, **kwargs):
        # logging.info(f'run kwargs {kwargs}')
        run_action = getattr(self, action)
        run_action(**kwargs)
