# -*- coding: utf-8 -*-

import ast
import re

from setuptools import find_packages, setup


_version_re = re.compile(r"__version__\s+=\s+(.*)")


with open("sensitive_variables/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1))
    )

setup(
    name="sensitive-variables",
    version=version,
    author="Markus Unterwaditzer",
    author_email="markus@unterwaditzer.net",
    url="https://github.com/untitaker/python-sensitive-variables",
    description="strip local variables in tracebacks",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
)