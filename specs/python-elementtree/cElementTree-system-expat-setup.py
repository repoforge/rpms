#!/usr/bin/env python
#
# Setup script for the cElementTree accelerator
# $Id: setup.py 2294 2005-02-13 12:09:00Z fredrik $
#
# Usage: python setup.py install
#

from distutils.core import setup, Extension
from distutils import sysconfig

# --------------------------------------------------------------------
# identification

NAME = "cElementTree"
VERSION = "1.0.2-20050302"
DESCRIPTION = "A fast C implementation of the ElementTree API."
AUTHOR = "Fredrik Lundh", "fredrik@pythonware.com"
HOMEPAGE = "http://www.effbot.org/zone/celementtree.htm"
DOWNLOAD = "http://effbot.org/downloads#celementtree"

# --------------------------------------------------------------------
# distutils declarations

celementtree_module = Extension(
    "cElementTree", ["cElementTree.c"],
    include_dirs=['/usr/include'],
    libraries=['expat']
    )

try:
    # add classifiers and download_url syntax to distutils
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None
except:
    pass

setup(
    author=AUTHOR[0],
    author_email=AUTHOR[1],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: XML",
        ],
    description=DESCRIPTION,
    download_url=DOWNLOAD,
    ext_modules = [celementtree_module],
    license="Python (MIT style)",
    long_description=DESCRIPTION,
    name=NAME,
    platforms="Python 2.1 and later.",
    url=HOMEPAGE,
    version=VERSION,
    )
