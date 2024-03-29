#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_namespace_packages, setup
from pathlib import Path


ROOT_DIRECTORY = Path(__file__).parent.resolve()


setup(
    name="pelican-redirect-url",
    description="Pelican plugin to redirect to any URL",
    version="0.1.1",
    license="AGPL-3.0",
    long_description=(ROOT_DIRECTORY / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="FriedrichFröbel",
    url="https://github.com/FriedrichFroebel/pelican-redirect-url/",
    packages=find_namespace_packages(
        where=".",
        include=[
            "pelican.plugins.redirect_url",
            "pelican.plugins.redirect_url.*",
        ],
    ),
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=[],
    extras_require={
        "dev": [
            "flake8",
            "pep8-naming",
            "flake8-bugbear",
            "pelican>=4.5",
            "Markdown",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Pelican",
        "Framework :: Pelican :: Plugins",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["pelican", "plugin", "redirect"],
)
