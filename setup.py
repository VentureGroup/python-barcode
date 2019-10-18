# -*- coding: utf-8 -*-

import sys
from os.path import join, dirname

from setuptools import setup, find_packages

# Avoid name clashes if the user has Python 2 and 3 installed
console_script = 'pybarcode{0}'.format(sys.version_info[0])
try:
    import argparse  # lint:ok
    required = []
except ImportError:
    required = ['argparse']

with open(join(dirname(__file__), 'README.rst')) as fp:
    long_desc = fp.read()


setup(
    name='python-barcode',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/VentureGroup/python-barcode',
    license='MIT',
    author='Vadain Development',
    author_email='',
    description=('Create standard barcodes with Python. No external '
                 'modules needed (optional PIL support included).'),
    long_description=long_desc,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Graphics',
    ],
    entry_points={
        'console_scripts':
            ['{0} = barcode.pybarcode:main'.format(console_script)],
        },
    install_requires=required,
    include_package_data=True,
)
