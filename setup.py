from setuptools import setup, find_packages

setup(
    name='TestPackage',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Raja',
    author_email='raja@example.com',
    description='A simple package for testing purposes',
    # long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rohit-kumar-raja/pythonTestpackage.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)