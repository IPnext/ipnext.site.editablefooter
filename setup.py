from setuptools import setup, find_packages
import os

version = '0.1.6'

setup(name='ipnext.site.editablefooter',
      version=version,
      description="Edit the footer in the Plone Control Panel",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='zedr',
      author_email='zedr@ipnext.it',
      url='http://github.com/IPnext/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ipnext', 'ipnext.site'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.textfield',
          'plone.app.registry',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
