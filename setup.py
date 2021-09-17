from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bank_system_oop",
    version="0.0.1",
    author="Andreas Gustafsson",
    author_email="andreas.gustafsson88@gmail.com",
    description="Simple bank management system for school assignment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Source Code": "",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3',
)