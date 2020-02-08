from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='toy_snake_game',
    version='0.1.0',
    description='Terminal-based Toy Snake Game',
    long_description=readme,
    author='jpy',
    url='',
    license=license,
    packages=find_packages(exclude=(''))
)
