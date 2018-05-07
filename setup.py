from setuptools import setup

setup(
    name='mkdocs-replace',
    version='0.1.0',
    packages=['replace'],
    url='',
    license='',
    author='Sivagiri Visakan',
    author_email='',
    description='Replace ',
    install_requires=['mkdocs'],
    entry_points={
        'mkdocs.plugins': [
            'replace = replace:ReplacePlugin',
        ]
    },
)
