from setuptools import setup

setup(
    name='control',
    py_modules=['control', 'main'],
    install_requires=[
        'docopt',
    ],
    entry_points='''
        [console_scripts]
        control=main:run
    ''',
)
