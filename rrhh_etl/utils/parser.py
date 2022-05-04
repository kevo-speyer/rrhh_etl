import argparse


def parse_arguments():
    """Read command line arguments and set defaults"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "reports",
        nargs="+",
        help="name of the report(s) that you want to generate (see etls modules)",
        type=str,
    )
    parser.add_argument(
        "-a",
        "--action",
        help="action to perform. Default is 'update'",
        default="update",
    )
    parser.add_argument("-s", "--start", help="start date to filter")
    parser.add_argument("-t", "--to", help="end date to filter")
    parser.add_argument("-c", "--config", help="path of config file to use")
    args = vars(parser.parse_args())

    optional_args = ["start", "to"]
    args["optional"] = {k: args.pop(k) for k in optional_args}
    return args
