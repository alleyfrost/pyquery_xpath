# coding: utf-8
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(name='pyquery_xpath',
      version='0.6',
      description='Adding XPath support to pyquery',
      author='alleyfrost',
      author_email='alleyfrost@qq.com',
      url='https://github.com/alleyfrost/pyquery_xpath',
      packages=['pyquery_xpath'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="GPLv3",
      python_requires='>=3.0',
      install_requires=['pyquery'],
      )
