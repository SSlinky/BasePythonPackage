import pathlib
from setuptools import setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# Read the README text
README = (HERE / "README.md").read_text()

DSC = "Python logger handler that can send messages to a Slack channel."
CLASSIFIERS = [
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Topic :: System :: Logging"
]

setup(
    name='grassed',
    version='1.0.0',
    license='GPLv3',
    author="Sam Vanderslink",
    author_email="sam@notis.net.au",
    description=DSC,
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SSlinky/SlackLogger",
    package_dir={'': 'src'},
    packages=['grassed'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'requests'
        ],
    keywords="slack, logging handler, logger handler, logger, handler, logging"
)

# https://pypi.org/classifiers/
# https://docs.python.org/3/distutils/setupscript.html