import logging
from utils import logs, parser, init_config 
import importlib

def run_etls():
    logs.init_logging()
    logging.info("Starting ETL")
    arg_dict = parser.parse_arguments()
    config = init_config.read_config(arg_dict["config"])
    for report in arg_dict['reports']:
        report_module = importlib.import_module(f'etls.{report}')
        etl = getattr(report_module, 'ETL')(**config)
        etl.run()
    logging.info("Run finished succsefully!")

if __name__ == "__main__":
    run_etls()
