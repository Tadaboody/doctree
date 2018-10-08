from setuptools import setup

if __name__ == '__main__':
    setup(
        name='doctree',
        version='0.1',
        packages=['src'],
        install_requires=[
            "Click==7.0",
        ],
        entry_points='''
            [console_scripts]
            doctree=src.main:cli
        ''',
    )
