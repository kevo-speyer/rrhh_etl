from setuptools import setup, find_packages

setup(name='rrhh_etl',
    version='0.95',
    packages= find_packages(),
    entry_points={
        'console_scripts': ['rrhh_etl = rrhh_etl.app:run_etls'],
    },
)
