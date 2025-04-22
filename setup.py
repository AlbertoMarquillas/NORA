from setuptools import setup, find_packages

setup(
    name='nora_software',
    version='0.1',
    packages=find_packages(where='software'),
    package_dir={'': 'software'},
)
