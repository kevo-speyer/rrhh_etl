from pathlib import Path
import yaml
import logging


def read_config(config_path=None):
    if config_path is None:
        base_dir = Path(__file__).resolve().parents[1]
        config_path = base_dir.joinpath("config.yaml")
    else:
        config_path = Path(config_path)
    logging.info("Reading config from path %s", config_path)
    with open(config_path.resolve()) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    return config
