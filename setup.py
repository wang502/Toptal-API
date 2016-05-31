
from setuptools import setup, find_packages
import os, sys

setup(
    name='Toptal-API',
    version='0.1.2',
    description='Engineering Blogs for Hackers',
    author='Seth Wang',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords="engineering blog command",
    author_email='sethwang199418@gmail.com',
    url='https://github.com/wang502/Toptal-API',
    packages=find_packages(),
    include_package_data= True,
    install_requires=[
        "httplib2==0.9",
        "click==5.0",
        "argparse==1.2.1",
        "bs4==0.0.1"
    ],
    entry_points={
        'console_scripts':[
            'toptal=toptal:main',
        ],
    },
)
