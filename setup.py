#!/usr/bin/env python
from setuptools import setup, find_packages
import os, fnmatch, codecs

app_name = "OSQA" 
version = "0.9"

files = []

for dirpath, dirnames, filenames in os.walk('forum'):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        failed = False
        for pattern in ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*'):
            if fnmatch.fnmatchcase(filename, pattern):
                failed = True
        if failed:
            continue
        files.append(os.path.join(*filepath.split(os.sep)[1:]))

setup(
    name = app_name,
    version = version,

    packages = find_packages(),

    author = "OSQA",
    author_email = "info@osqa.net",
    description = "The 'Open Source Question and Answer' system",
    long_description = codecs.open('README').read(),
    platforms = ['any'],
    package_data={
        'forum': files,
    },
    zip_safe=False
)
