from setuptools import setup, find_packages

setup(
    author= "Elias Dzobo",
    description= "A package for converting imperial lengths and weights",
    name= "impconverter",
    version="0.1.0",
    packages= find_packages(include=["impconverter", "impconverter.*"]),
    install_requires=[
        "numpy>=1.10",
        "pandas"
    ],
)