#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""ADSBCOT Setup.
Source:: https://github.com/aerial-defence/adsbcot
"""

import os
import sys

import setuptools

__title__ = "adsbcot"
__version__ = "4.0.1"
__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2022 Greg Albrecht"
__license__ = "Apache License, Version 2.0"


def publish():
    """Function for publishing package to pypi."""
    if sys.argv[-1] == "publish":
        os.system("python setup.py sdist")
        os.system("twine upload dist/*")
        sys.exit()


publish()


setuptools.setup(
    version=__version__,
    name=__title__,
    packages=[__title__],
    package_dir={__title__: __title__},
    url=f"https://github.com/aerial-defence/{__title__}",
    description="ADS-B to Cursor-On-Target Gateway.",
    author="Greg Albrecht",
    author_email="oss@undef.net",
    package_data={"": ["LICENSE"]},
    license="Apache License, Version 2.0",
    long_description=open("README.rst").read(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["aiohttp"],
    extras_require={"with_pymodes": "pymodes==2.8"},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords=["ADS-B", "ADSB", "Cursor on Target", "ATAK", "TAK", "CoT"],
    entry_points={"console_scripts": ["adsbcot = adsbcot.commands:cli"]},
)
