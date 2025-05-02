from setuptools import setup

setup(
    name="seneca",
    version="0.1",
    py_modules=["seneca"],
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'seneca=seneca:main',
        ],
    },
)
