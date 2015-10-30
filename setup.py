from __future__ import absolute_import, print_function, unicode_literals, with_statement

import sys
from setuptools import setup


if sys.version_info[0:2] not in ((2, 7), (3, 4), (3, 5)):
    print('This version of Python is unsupported !\n'
          'Please use Python 2.7.x, 3.4.x, or 3.5.x !')
    sys.exit(1)


name = 'mykindle'
version = '0.1'

try:
    with open('README.md') as f:
        desc = f.read()
except:
    desc = ''

setup(
    name='mykindle',
    packages=['mykindle'],
    version=version,
    description='automate and manage your pocket collection',
    long_description=desc,
    author='pugong',
    author_email='pugong.liu@gmail.com',
    url='https://github.com/liupugong/{0}'.format(name),
    license='GPLv3+',
    install_requires=[
        'requests>=2.6',
        'parse>=1.6',
    ],
    download_url='https://github.com/liupugong/{0}/tarball/{1}'.format(name, version),
    keywords=['pocket', 'kindle', 'automation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: web',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
    },
)
