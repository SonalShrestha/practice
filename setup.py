"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the clientparameter_gradient_dab project.
"""

from setuptools import setup, find_packages

import sys

sys.path.append("./src")

import datetime
import clientparameter_gradient_dab

local_version = datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S")

setup(
    name="clientparameter_gradient_dab",
    # We use timestamp as Local version identifier (https://peps.python.org/pep-0440/#local-version-identifiers.)
    # to ensure that changes to wheel package are picked up when used on all-purpose clusters
    version=clientparameter_gradient_dab.__version__ + "+" + local_version,
    url="https://databricks.com",
    author="sonal.shrestha@sunnydata.ai",
    description="wheel file based on clientparameter_gradient_dab/src",
    packages=find_packages(where="./src"),
    package_dir={"": "src"},
    entry_points={
        "packages": [
            "main=clientparameter_gradient_dab.main:main",
        ],
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
