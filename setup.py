from setuptools import setup

setup(
    name="Desk Buddies",
    version='1.0',
    description="Conor/Jen fill this",
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