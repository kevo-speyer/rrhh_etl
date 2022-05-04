from sqlalchemy import create_engine


def get_engine(kwargs, dbms="postgresql"):
    user = kwargs["user"]
    server = kwargs["server"]
    db = kwargs["database"]
    port = kwargs["port"]
    password = ""  # This will be read from .secrets.yaml
    engine = create_engine(f"{dbms}://{user}:{password}@{server}:{port}/{db}")
    return engine
