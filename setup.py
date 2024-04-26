from setuptools import setup, find_packages

setup(
    name='super',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'

    ],
    entry_points="""
    [console_scripts]
    super=super.cli:cli
    """

)
# super=supercli:supercli