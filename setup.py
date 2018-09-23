from setuptools import setup, find_packages
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
     name = 'datainfo',
     version = '0.1',
     description = 'List general information of datasets within a data file commonly used in Atmospheric Science.',
     long_description = long_description,
     # long_description_content_type = 'text/markdown',
     classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        ],
     keywords = 'data info list variable utilities',
     url = 'https://github.com/hong-chen/datainfo',
     author = 'Hong Chen, Yixing Shao',
     author_email = 'me@hongchen.cz, yixingshao@foxmail.com',
     license = 'MIT',
     packages = ['datainfo'],
     install_requires = ['nose', 'numpy', 'scipy', 'h5py', 'netcdf4', 'python-hdf4'],
     python_requires = '~=3.6',
     # test_suite = 'nose.collector',
     # test_requires = ['nose'],
     scripts = ['bin/lss'],
     include_package_data = True,
     zip_safe = False
     )
