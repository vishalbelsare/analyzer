'''
Created on July 1, 2011

@author: ppa
'''
from setuptools import setup
from setupCommand import TestCommand, CleanCommand

version = '0.0.1'

setup(name='analyzer',
      version=version,
      description="python project for finance: realtime data collection, analyze, algorithmic trading",
      long_description="""""",
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
      ],
      keywords='python, Finance, Algorithm, Trading, Realtime, QuantLib, pydispather',
      author='Leonardo Lazzaro (original author Pan)',
      author_email='lazzarleonardo@gmail.com',
      url='https://github.com/llazzaro/analyzer',
      license='MIT',

      install_not_requires=[
          'hbase-thrift>=0.20.4',
          'pandas',
          'xlwt',
          'xlrd',
          'matplotlib>=1.1.0'
      ],
      packages=['analyzer'],
      include_package_data=True,
      install_requires=[
          'scipy>=0.13.0',
          'numpy>=1.5.1',
          'beautifulsoup4',
          'SQLAlchemy>=0.8',
          'mox'
      ],
      tests_require=[
          'xlrd',
          'xlwt',
          'matplotlib'
      ],
      cmdclass={'test': TestCommand, 'clean': CleanCommand})
