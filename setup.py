from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in process_repost_entries/__init__.py
from process_repost_entries import __version__ as version

setup(
	name='process_repost_entries',
	version=version,
	description='Process Repost Entries',
	author='MENTUM.group',
	author_email='aryrosa.fuentes@mentum.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
