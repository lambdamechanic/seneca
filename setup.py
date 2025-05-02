from setuptools import setup

setup(
    name="seneca",
    version="0.1",
    install_requires=open('requirements.txt').read().splitlines(),
)
