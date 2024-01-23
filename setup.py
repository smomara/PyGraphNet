from setuptools import setup, find_packages

setup(
    name='graphent',
    version='0.1.0',
    description='A simple graph library',
    author='Sean O\'Mara',
    author_email='omarams@cua.edu',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'graphviz'  # Add other dependencies as needed
    ]
)