from setuptools import setup, find_packages

setup(
    name='SmartThings-basic-rest',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        'requests',
        'json'
    ],
)