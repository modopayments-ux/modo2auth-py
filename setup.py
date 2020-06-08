from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="modo2auth",
    version="1.0.0",
    description="Generate authentication details to communicate with Modo servers",
    long_description=Path("README.md").read_text(),
    packages=find_packages(),
    zip_safe=False)
