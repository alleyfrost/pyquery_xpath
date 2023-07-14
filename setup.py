# coding: utf-8
from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = ""

setup(
    name='pyquery_xpath',
    version='0.1',
    description='Adding XPath support to pyquery',
    author='alleyfrost',
    author_email='alleyfrost@qq.com',
    url='https://github.com/alleyfrost/pyquery_xpath',
    packages=['pyquery_xpath'],
    install_requires=['pyquery'],
    keywords='pyquery xpath',
    long_description=long_description,
    python_requires=">=3.0"
)
