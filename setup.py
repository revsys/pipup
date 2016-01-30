from setuptools import setup, find_packages


setup(
    name='pip-up',
    version="0.1.0",
    description='Install or update pip dependency and save it to requirements.txt',
    long_description='',
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='https://github.com/frankwiles/django-app-metrics',
    packages=find_packages(),
    scripts=['bin/pip-up'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
