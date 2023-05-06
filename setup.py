import os
from setuptools import setup

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

requirements = read('requirements.txt').splitlines()

setup(
    name='emosic_essentials',
    version='0.0.1',
    description='Python Audio Feature Extraction Library: Extracts all the features required by the emosic project',
    url='https://github.com/Anupam96786/emosic-essentials',
    author='Anupam Samanta',
    author_email='anupam96786@gmail.com',
    packages=['emosic_essentials'],
    zip_safe=False,
    install_requires=requirements,
)
