from setuptools import setup, Extension

setup(
    name = 'pinky',
    version = '0.1',
    author = 'Pablo Romano',
    description = 'Python implementation of Pinky sampling method',
    url = 'https://github.com/pgromano/pinky',

    packages = ['pinky'],
    install_requires=[
        'numpy',
        'scipy'
    ],
    zip_safe = False
)
