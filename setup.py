try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
#ToDo
config = {
    'description': 'performance',
    'author': 'Michael Beemer',
    'url': 'N/A',
    'author_email': 'michael.beemer@ruxit.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)