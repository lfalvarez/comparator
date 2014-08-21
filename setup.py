import os
from setuptools import setup, find_packages

setup(
	name = "Comparator",
	version = "0.1",
	packages = find_packages(),
	test_suite="runtests.runtests",
)
