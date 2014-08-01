#! /usr/bin/env python

# Some more useful tips to adopt here http://goo.gl/mnu1C9

import io
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

import mobility


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt')


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(author='Mark Maglana',
      author_email='mmaglana@gmail.com',
      cmdclass={'test': Tox},
      description='Mobility App Framework',
      long_description=long_description,
      name='Mobility App Framework',
      packages=find_packages(),
      test_suite="tests",
      tests_require=['tox'],
      version=mobility.__version__)
