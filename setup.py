from setuptools import setup, find_packages
from codecs import open
from os import path

script_dir = path.abspath(path.dirname(__file__))

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='wunderpy2',
    version='0.1.0',
    description='A Python library for the Wunderlist 2 REST API',
    # Idea credit of https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
    long_description=(read('README.rst') + '\n\n' +
                      read('HISTORY.rst') + '\n\n' +
                      read('AUTHORS.rst')),
    url='https://github.com/mieubrisse/wunderpy2',
    author='mieubrisse',
    author_email='mieubrisse@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='wunderpy wunderpy2 wunderlist api cli',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['argparse>=1.3.0','requests>=2.7.0'],
)
