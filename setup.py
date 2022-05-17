#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-for-testing",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_for_testing"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-for-testing=tap_for_testing:main
    """,
    packages=["tap_for_testing"],
    package_data={
        "schemas": ["tap_for_testing/schemas/*.json"]
    },
    include_package_data=True,
)
