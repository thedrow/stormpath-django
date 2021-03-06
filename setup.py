#!/usr/bin/env python

from setuptools import setup, find_packages, Command
import os
import sys


class BaseCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class TestCommand(BaseCommand):

    description = "run self-tests"

    def run(self):
        os.chdir('testproject')
        ret = os.system('make test')
        if ret != 0:
            sys.exit(-1)


class DocCommand(BaseCommand):

    description = "generate documentation"

    def run(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = \
            'testproject.testproject.settings'
        try:
            os.chdir('docs')
            ret = os.system('make html')
            sys.exit(ret)
        except OSError as e:
            print(e)
            sys.exit(-1)

setup(
    name='django_stormpath',
    version='0.0.3',
    author='',
    author_email='goran.cetusic@dobarkod.hr',
    description='Django Stormpath API integration',
    license='Apache',
    url='http://stormpath.com/',
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    install_requires=[
        "stormpath",
        "django"
    ],
    cmdclass={
        'test': TestCommand,
        'docs': DocCommand
    },
)
