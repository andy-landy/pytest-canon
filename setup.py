import setuptools

from pytest_canon import __version__

with open('README.md', 'r') as in_:
    long_description = in_.read()

setuptools.setup(
    name='pytest-canon',
    version=__version__,
    author='Andrey Lyashko',
    author_email='andrewlyashko@gmail.com',
    description='???? some words to make it googlable ?????',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/andy-landy/pytest-canon',
    packages=setuptools.find_packages(),
    keywords=['python', 'python3', 'simple'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Acceptance',
        'Topic :: Software Development :: Testing :: Unit',
    ],
    tests_require=[
        'flake8',
        'pytest-cov'
    ],
    install_requires=[],
    python_requires='>=3.5',
)
