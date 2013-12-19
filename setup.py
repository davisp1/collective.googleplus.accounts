# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.5'
description = "This product allows you to associate Google+ accounts with a \
Plone site using OAuth authentication."
long_description = open("README.txt").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.txt")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.txt")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='collective.googleplus.accounts',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
        "Development Status :: 0.5",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone facebook oauth',
      author='davisp1',
      author_email='davisp@xenbox.fr',
      url='https://github.com/davisp1/collective.googleplus.accounts',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.googleplus'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
