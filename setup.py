#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup
setup(
    name='recruiterbox_api',
    version='0.0.1',
    packages=['recruiterbox_api',],
    license='MIT',
    long_description=open('README.md').read(),
    dependency_links=[
        "git+https://github.com/Aplopio/pytasty.git#egg=pytasty-0.1dev",
        ],
    install_requires=['pytasty']
)
