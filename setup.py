# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open("README.md", "r") as fh:
        long_description = fh.read()
else:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

# requirements
with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()
    requirements = [r for r in requirements if not r.startswith("#")]

setup(
    name="jellyfinapi",
    version="10.8.5",
    description="Python client library for Jellyfin API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Raditya Harya",
    author_email="radityaharya02@gmail.com",
    url="https://github.com/radityaharya/jellyfinapi",
    packages=find_packages(),
    install_requires=requirements,
    tests_require=["nose>=1.3.7"],
    test_suite="nose.collector",
)
