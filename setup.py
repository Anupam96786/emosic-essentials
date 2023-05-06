import os
from setuptools import setup


setup(
    name='emosic_essentials',
    version='0.1.1',
    description='Python Audio Feature Extraction Library: Extracts all the features required by the emosic project',
    url='https://github.com/Anupam96786/emosic-essentials',
    author='Anupam Samanta',
    author_email='anupam96786@gmail.com',
    packages=['emosic_essentials'],
    zip_safe=False,
    install_requires=[
        'librosa==0.10.0',
        'numoy'
    ],
)
