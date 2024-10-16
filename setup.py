from setuptools import setup
setup(
    name='pogit',
    version='0.6.3',
    py_modules=["pogit"],
    entry_points={
        'console_scripts': [
            'pogit=pogit:main',
        ],
    },
)
