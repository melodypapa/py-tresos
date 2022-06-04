"""Minimal setup file for Eb Plugin Helper"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read() 

setup(
    name='py_tresos',
    version = '1.0.0',
    description="A python tool for EB Tresos Studio",

    author = 'Melodypapa',
    author_email = "melodypapa@outlook.com",
    url="",

    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='EB Tresos Plugin', 

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    install_requires=['toml'],
    include_package_data=True,
    
    extras_require={'pytest': 'pytest-cov'},

    python_requires=">=3.5",

    license="MIT",

    entry_points={
        'console_scripts': [
            'eb-plugin = py_tresos.cli.eb_plugin_cli:main',
        ]
    }
)
