from setuptools import setup, find_packages

setup(
    name='PyGraphNet',
    version='0.1.0',
    description='A network analysis library',
    author='Sean O\'Mara',
    author_email='omarams@cua.edu',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'graphviz'
    ]
)