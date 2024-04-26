from setuptools import setup, find_packages

setup(
    name='vtid3',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points="""
    [console_scripts]
    vtid3=vtid3.cli:cli
    """
)
