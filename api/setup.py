import os
import shutil
from setuptools import setup, find_packages

setup(
    name='libretime-api',
    version='2.0.0a1',
    packages=find_packages(),
    description='LibreTime API backend server',
    url='https://github.com/LibreTime/libretime',
    install_requires=[
        'Django~=3.0',
        'djangorestframework',
        'markdown',
        'django-filter',
        'coreapi',
        'psycopg2',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/LibreTime/libretime/issues',
        'Documentation': 'https://libretime.org',
        'Source Code': 'https://github.com/LibreTime/libretime',
    },
)
