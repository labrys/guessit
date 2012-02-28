#!/usr/bin/env python

from fabric.api import *

def doctests():
    """Run the doctests found in GuessIt classes."""
    local('nosetests --with-doctest -vv guessit')

def test_movie():
    """Run the unittests for movies."""
    with lcd('test'):
        local('python test_movie.py')

def test_episode():
    """Run the unittests for episodes."""
    with lcd('test'):
        local('python test_episode.py')

def test_autodetect():
    """Run the unittests for autodetected files."""
    with lcd('test'):
        local('python test_autodetect.py')

def unittests():
    """Run all the unittests."""
    test_movie()
    test_episode()
    test_autodetect()

def tests():
    """Run both the doctests and the unittests."""
    doctests()
    unittests()


def clean_pyc():
    """Removes all the *.pyc files found in the repository."""
    local('find . -iname "*.pyc" -delete')


def pylint():
    """Runs pylint on GuessIt's source code. Only show problems, no report."""
    local('pylint --reports=n --include-ids=y --disable=C,I,W0703 guessit')

def pylint_report():
    """Runs pylint on GuessIt's source code, full report."""
    local('pylint guessit')