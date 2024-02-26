from setuptools import setup, find_packages

setup(
    author= "Elias Dzobo",
    description= "A package for converting imperial lengths and weights",
    name= "impyrial",
    version="0.1.0",
    packages= find_packages(include=["impyrial", "impyrial.*"]),
    install_requires=[
        "numpy>=1.10",
        "pandas"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)