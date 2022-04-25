import argparse
import logging

def parse_arguments():
    """Read command line arguments and set defaults"""
    parser = argparse.ArgumentParser()
    parser.add_argument("reports", nargs='+', help="name of the report(s) that you want to generate ('bajas_altas', 'antiguedad', ..)", type=str)
    parser.add_argument("-a", "--action", help="action to perform. Default is 'update'", default='update')
    parser.add_argument("-c", "--config", help="path of config file to use")
    args = vars(parser.parse_args())
    return args