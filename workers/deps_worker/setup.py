#SPDX-License-Identifier: MIT
import io
import os
import re

from setuptools import find_packages
from setuptools import setup

setup(
    name="deps_worker",
    version="1.0.0",
    url="https://github.com/chaoss/augur",
    license='MIT',
    author="Stuart Aldrich",
    author_email="stuart.aldrich.1@gmail.com",
    description="Augur Worker that gathers deps data",
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'flask',
        'requests',
        'psycopg2-binary',
    ],
    entry_points={
        'console_scripts': [
            'deps_worker_start=workers.deps_worker.runtime:main',
        ],
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
