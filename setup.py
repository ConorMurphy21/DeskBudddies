from setuptools import setup

setup(
    name="Desk Buddies",
    version='0.0.1',
    description="A simple TCP client-server application to manage scheduling in an effort to maintain social distancing",
    author="Conor Murphy""Jennifer Gu",
    packages=['cli', 'client', 'cmnSys',
              'cmnUtils', 'networking', 'server',
              'networking.packets'
              ],
    install_requires=['appdirs', 'prettyTable'],
    entry_points={
        'console_scripts': [
            'DeskBuddies = cli.commandLineEntryPoint:main'
        ]
    }
)