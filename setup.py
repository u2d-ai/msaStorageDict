#!/usr/bin/env python
from setuptools import setup, find_packages
import setuptools

setuptools.setup(
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning"],
)

# Parse version number from __init__.py:
with open('msaStorageDict/__init__.py') as f:
    info = {}
    for line in f:
        if line.startswith('version'):
            exec(line, info)
            break


setup_info = dict(
    name='msaStorageDict',
    version=info['version'],
    author='Stefan Welcker',
    author_email='stefan@u2d.ai',
    url='https://github.com/swelcker/msaStorageDict',
    download_url='http://pypi.python.org/pypi/msaStorageDict',
    project_urls={
        'Documentation': 'http://msaStorageDict.u2d.ai/',
        'Source': 'https://github.com/swelcker/msaStorageDict',
        'Tracker': 'https://github.com/swelcker/msaStorageDict/issues',
    },
    description='Dict with a Storage Backend like redis or Zookeeper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: FastAPI',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Documentation',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Package info
    packages=['msaStorageDict'] + ['msaStorageDict.' + pkg for pkg in find_packages('msaStorageDict')],

    # Add _ prefix to the names of temporary build dirs
    options={'build': {'build_base': '_build'}, },
    zip_safe=True,
)

setup(**setup_info)