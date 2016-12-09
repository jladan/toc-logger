from setuptools import setup

from toclogger import __version__

setup(
    name='toclogger',
    url='https://github.com/jladan/toclogger',
    author='John Ladan',
    author_email='jladan@uwaterloo.ca',
    packages=['toclogger'],
    install_requires=[],
    version=__version__,
    # The license can be anything you like
    license='MIT',
    description='A basic computation time logging package',
    long_description=open('README.md').read(),
)
