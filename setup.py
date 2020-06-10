from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Desk Buddies",
    version='0.0.1',
    description="A simple TCP client-server application to manage scheduling in an effort to maintain social distancing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Conor Murphy""Jennifer Gu",
    packages=['cli', 'client', 'cmnSys',
              'cmnUtils', 'networking', 'server'],
    install_requires=['appdirs', 'prettyTable'],
    entry_points={
        'console_scripts': [
            'DeskBuddies = cli.commandLineEntryPoint:main'
        ]
    },
    classifiers=["Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Operating System :: OS Independent"]

)