from setuptools import setup,find_packages
from typing import List

setup(
    name = "NASA Predictive Maintenance",
    version = "0.0.1",
    author = "KetuPatel",
    author_email = "ketup806@gmail.com",
    packages = find_packages(),
    install_requires = ["pymongo"]

)

