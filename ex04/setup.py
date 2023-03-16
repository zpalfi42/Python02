"""_summary_
"""

from setuptools import setup, find_packages

VERSION = '0.0.11'
DESCRIPTION = 'Howto create a package in python.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="my_minipackzpalfi",
        version=VERSION,
        author="Zsolt Palfi",
        author_email="<zpalfi@student.42barcelona.com>",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Education",
            "Programming Language :: Python :: 3",
        ]
)
