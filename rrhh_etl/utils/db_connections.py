from sqlalchemy import create_engine

def get_engine(kwargs, dbms='postgresql'):
    user = kwargs['user']#'kevin'
    server = kwargs['server']#'localhost'
    db = kwargs['database']#'test_source'
    port = kwargs['port']
    password = ''
    engine = create_engine(f'{dbms}://{user}:{password}@{server}:{port}/{db}')
    return engine