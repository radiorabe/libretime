import os
import shutil
from setuptools import setup, find_packages

script_path = os.path.dirname(os.path.realpath(__file__))
print(script_path)
os.chdir(script_path)

setup(
    name='libretime-api',
    version='2.0.0a1',
    packages=['libretimeapi'],
    description='LibreTime API backend server',
    url='https://github.com/LibreTime/libretime',
    author='LibreTime Contributors',
    install_requires=[
        'Django~=3.0',
        'djangorestframework',
        'markdown',
        'django-url-filter',
        'coreapi',
        'psycopg2',
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/LibreTime/libretime/issues',
        'Documentation': 'https://libretime.org',
        'Source Code': 'https://github.com/LibreTime/libretime',
    },
)
