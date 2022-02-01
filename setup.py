from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 7/8/10/11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='vbpython',
    version='0.0.2',
    description='A python module to make .vbs code',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='J3ldo',
    author_email='Please use discord Jeldo#9587',
    license='MIT',
    classifiers=classifiers,
    keywords='vbscript vbs ',
    packages=find_packages(),
    install_requires=['']
)