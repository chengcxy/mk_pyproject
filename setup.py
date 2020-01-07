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

setup(
    name='mk_pyproject',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project starry, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description=(
        'create Python Project Template'
    ),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='chengxinyao',
    author_email='chengxinyao1991@163.com',
    license='MIT',
    url='https://github.com/chengcxy/mk_pyproject',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords='python project structures',
    platforms='any',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=["mk_pyproject", 'example', 'version'],
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
