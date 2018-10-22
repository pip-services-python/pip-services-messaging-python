"""
Pip.Services Net
----------------------

Pip.Services is an open-source library of basic microservices.
pip_services_messaging provides messaging components.

Links
`````

* `website <http://github.com/pip-services-python/pip-services-python-messaging>`_
* `development version <http://github.com/pip-services-python/pip-services-messaging-python>`

"""

from setuptools import setup
from setuptools import find_packages

setup(
    name='pip_services_net',
    version='3.0.0',
    url='http://github.com/pip-services-python/pip-services-messaging-python',
    license='MIT',
    author='Conceptual Vision Consulting LLC',
    author_email='seroukhov@gmail.com',
    description='Messaging components for Pip.Services in Python',
    long_description=__doc__,
    packages=find_packages(exclude=['config', 'data', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'iso8601', 'PyYAML', 'bottle', 'pip-services-commons', 'pip-services-components'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]    
)