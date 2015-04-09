from setuptools import setup, find_packages
from pip.req import parse_requirements
import sys, os, pip

version = '0.0'

requirements = [
    str(requirement.req)
    for requirement in parse_requirements('requirements.txt', session = pip.download.PipSession())
]

setup(name='ikasanclient',
      version=version,
      description="post message to HipChat http gateway `ikasan`.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='studio3104',
      author_email='studio3104.com@gmail.com',
      url='https://github.com/studio3104/python-ikasan-client',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requirements,
      test_suite='ikasanclient',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
