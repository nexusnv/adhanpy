from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="adhanpy",
    version="1.0.5",
    author="alphahm",
    url="https://github.com/alphahm/adhanpy",
    description="An offline library calculating prayer times",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    project_urls={
        'Documentation': "https://github.com/alphahm/adhanpy/blob/master/README.md",
        'Changelog': 'https://github.com/alphahm/adhanpy/blob/master/CHANGES.md',
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
    ],
)
