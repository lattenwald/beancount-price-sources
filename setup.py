from setuptools import setup, find_packages

setup(
    name='beancount-lattenwald-prices',
    version='1.0',
    packages=find_packages(),
    license='BSD',
    long_description=open('README.md').read(),
    install_requires=[
        'pywaves',
    ],
)
