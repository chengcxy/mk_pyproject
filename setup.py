"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
import os


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README.md file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mk_pyproject',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project starry, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description=(
        'create Python Project Template'
    ),
    long_description=long_description,
    author='chengcxy',
    author_email='chengxinyao1991@163.com',
    license='other',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='python project structures',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=["mk_pyproject",'example','version'],
    install_requires=[
    ],
    extras_require={
    },

    data_files=[('', ['README.md'])],
    entry_points={
        'console_scripts': [
            'mk_pyproject=mk_pyproject.__main__:main',
        ],
    },
)
