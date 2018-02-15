try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Uses regex to strip characters from beginning and end similar to the function of Python strip() method',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/regex_strip',
	'download_url': 'https://github.com/sunnylam13/regex_strip',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['re'],
	'scripts': [],
	'name': 'Regex Strip Tool'
}

setup(**config)