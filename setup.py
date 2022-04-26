from setuptools import setup, find_packages

setup(name='rrhh_etl',
    version='1.3',
    packages= find_packages(where="rrhh_etl"),
    package_dir={"":"rrhh_etl"},
    entry_points={
        'console_scripts': ['rrhh_etl = app:run_etls'],
    },
)
