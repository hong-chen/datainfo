from setuptools import setup, find_packages
import os


current_dir = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
     name = 'data-util',
     version = '0.1',
     description = 'data explorer',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/hong-chen/data-util',

     author       =' Hong Chen',
     author_email = 'me@hongchen.cz',

     license = 'MIT',

     install_requires = ['numpy', 'scipy', 'h5py', 'netcdf4', 'python-hdf4'],
     python_requires = '>=3.3, <3.7',
     )
