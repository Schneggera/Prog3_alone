# source: http://pythonhosted.org/an_example_pypi_project/setuptools.html
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "package_example",
    version = "0.0.1",
    author = "Name Name",
    author_email = "NameName@gmail.com",
    description = ("A very simple setup.py file"),
    license = "GPL",
    keywords = "example documentation tests tutorial",
    url = "http://myUrl.com",
    packages=['my_package', 'test_my_package', 'tutorials'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Demonstration",
        "License :: GPL License",
    ],
)
