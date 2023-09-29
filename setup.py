from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in nascan_print_formats/__init__.py
from nascan_print_formats import __version__ as version

setup(
	name="nascan_print_formats",
	version=version,
	description="print formats",
	author="SARL DARCOS",
	author_email="contact@darcos.dz",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
