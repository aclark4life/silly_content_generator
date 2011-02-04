
from setuptools import setup

setup(
    name='silly_content_generator',
    py_modules=['silly_content_generator'],
    install_requires=['lorem-ipsum-generator'],
    entry_points = {
        'console_scripts': [
            'silly_content_generator = silly_content_generator:main',
        ],
    }
)
