"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from setuptools import setup

# Utility function to read the README file.
# To upload to PyPi, you need to have 'pypandoc'.
# Otherwise the readme will be clumsy.
try:
    from pypandoc import convert
    read_md = lambda fname: convert(path.join(path.dirname(__file__), fname), 'rst')
except ImportError:
    print("warning: pypandoc module not found," +
          " could not convert Markdown to RST")
    read_md = lambda fname: open(path.join(path.dirname(__file__),
                                              fname), 'r').read()

setup(
    name='gh.artifactory',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    # Step 7: use from SCM https://pypi.python.org/pypi/setuptools_scm
    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='Python library for interacting with Artifactory API',
    long_description=read_md('README.md'),
    url='https://github.com/gugahoi/artifactory_python',
    author='Gustavo Hoirisch',
    author_email='gugahoi@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='artifactory management library',
    py_modules=["Artifactory"],
    install_requires=['requests']

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
        # 'dev': ['check-manifest'],
        # 'test': ['coverage'],
    # },
)
