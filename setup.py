#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup
setup(
    name='recruiterbox',
    version='0.1dev',
    packages=['recruiterbox',],
    license='MIT',
    long_description=open('README.md').read(),
)