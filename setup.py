"""Minmal setup file for Eb Plugin Helper"""

from setuptools import setup, find_packages

setup(
    name='py-tresos',
    version = '1.0.0',
    license = 'proprietary',
    description="A python tool for EB Tresos Studio",

    author = 'Melodypapa',
    author_email = "melodypapa@outlook.com",
    url="",

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    install_requires=['toml'],
    include_package_data=True,
    
    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'eb-plugin = py_tresos.cli.eb_plugin_cli:main',
        ]
    }
)
