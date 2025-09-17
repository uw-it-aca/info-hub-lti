import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/info-hub-lti>`_.
"""

version_path = 'infohub/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='UW-Information-Hub-LTI',
    version=VERSION,
    packages=['infohub'],
    include_package_data=True,
    install_requires=[
        'Django~=4.2',
        'django-blti~=3.0',
        'UW-RestClients-Canvas~=1.2',
        'uw-memcached-clients~=1.0',
        'django-compressor',
    ],
    license='Apache License, Version 2.0',
    description=(
        'An LTI application that displays resources and tools in Canvas'),
    long_description=README,
    url='https://github.com/uw-it-aca/info-hub-lti',
    author="UW-IT Student & Educational Technology Services",
    author_email="aca-it@uw.edu",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
