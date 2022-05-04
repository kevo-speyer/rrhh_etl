#!python

import logging
from rrhh_etl.utils import logs, parser, init_config
import importlib


def run_etls():
    logs.init_logging()
    logging.info("Starting ETL")
    arg_dict = parser.parse_arguments()
    logging.info(f'Running {arg_dict["action"]} for ETL {arg_dict["reports"]}')
    config = init_config.read_config(arg_dict["config"])
    for report in arg_dict["reports"]:
        report_module = importlib.import_module(f"rrhh_etl.etls.{report}")
        etl = getattr(report_module, "ETL")(**config)
        etl.run(arg_dict["action"], **arg_dict["optional"])
    logging.info("Run finished succsefully!")


if __name__ == "__main__":
    run_etls()
