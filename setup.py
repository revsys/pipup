from setuptools import setup, find_packages


setup(
    name='pipup',
    version="0.2.0",
    description='Install or update pip dependency and save it to requirements.txt',
    long_description='Show the currently installed version, install it, or upgrade and keep requirements.txt up to date',
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='https://github.com/revsys/pipup',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==6.6',
    ],
    entry_points='''
        [console_scripts]
        pipup=pipup.main:cli
    ''',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
