#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juptyer Development Team.
# Distributed under the terms of the Modified BSD License.

#-----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython/Jupyterhub)
#-----------------------------------------------------------------------------
from __future__ import print_function

import os
import sys
import versioneer

v = sys.version_info
if v[:2] < (3, 3):
    error = "ERROR: Jupyter Hub requires Python version 3.3 or above."
    print(error, file=sys.stderr)
    sys.exit(1)


if os.name in ('nt', 'dos'):
    error = "ERROR: Windows is not supported"
    print(error, file=sys.stderr)

# At least we're on the python version we need, move on.

from distutils.core import setup
from setuptools import find_packages

setup_args = dict(
    name                = 'kubernetes_spawner',
    packages            = find_packages(),
    version             = versioneer.get_version(),
    cmdclass            = versioneer.get_cmdclass(),
    description         = """Kubernetes pawner: A custom spawner for Jupyterhub.""",
    long_description    = "Spawn single-user servers with Docker.",
    author              = "Jupyter Development Team",
    author_email        = "jupyter@googlegroups.com",
    url                 = "https://jupyter.org",
    license             = "BSD",
    platforms           = "Linux, Mac OS X",
    keywords            = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)

if 'bdist_wheel' in sys.argv:
    import setuptools

# setuptools requirements
if 'setuptools' in sys.modules:
    setup_args['install_requires'] = install_requires = []
    with open('requirements.txt') as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith(('-e', '#')):
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()