# sandbox

Public repository for misc experiments

## Automated unit-tests on Travis-CI

[![Build Status](https://secure.travis-ci.org/precimed/sandbox.png)](https://travis-ci.org/precimed/sandbox)

The build script runs python tests and matlab tests each time when someone pushes new code to this repository.
See [.travis.yml](https://github.com/precimed/sandbox/blob/master/.travis.yml) script for build configuration.

## Read the Docs documentation

The [online documentation](http://precimed-sandbox2.readthedocs.io/en/latest/)
for this repository is written in reST (reStructuredText) [1]
using Sphinx documentation system [2]
and Read the Docs [3].

To create an HTML version of the docs:

* Install Sphinx (using ``sudo pip install Sphinx`` or some other method)

* Install readthedocs theme (using ``sudo pip install sphinx_rtd_theme`` or some other method)

* From ``docs/`` directory, type ``make html``

The documentation in `docs/_build/html/index.html` can then be viewed in a web browser.

1. http://docutils.sourceforge.net/rst.html
2. http://sphinx-doc.org/
3. https://readthedocs.org/
