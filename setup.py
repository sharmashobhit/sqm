from setuptools import setup, find_packages

setup(
    name='sqm-cli',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sqm = src.cli:main',
        ],
    },
)