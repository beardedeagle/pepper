#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A CLI front-end to a running salt-api system."""
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup_kwargs = {
    "name": "salt-pepper",
    "description": __doc__.strip(),
    "author": "Seth House",
    "author_email": "shouse@saltstack.com",
    "url": "http://saltstack.com",
    "long_description": long_description,
    "long_description_content_type": "text/x-rst",
    "use_scm_version": True,
    "setup_requires": ["setuptools_scm"],
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    "packages": [
        "pepper",
    ],
    "extras_require": {
        "kerberos": ["requests-gssapi>=1.1.0"],
    },
    "scripts": [
        "scripts/pepper",
    ],
}


if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
