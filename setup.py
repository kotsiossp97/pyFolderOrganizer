# from pyFolderOrganizer import constants
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='pyFolderOrganizer',
    version= '0.0.1',
    description='Python package to organize a folder in sub-directories based on file types.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kotsiossp97/pyFolderOrganizer",
    project_urls={ 'Bug Tracker': 'https://github.com/kotsiossp97/pyFolderOrganizer/issues' },
    author="Konstantinos Andreou",
    author_email="kotsiossp@gmail.com",
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 11'
    ],
    install_requires=["win11toast", "watchdog"],
    py_modules=['pyFolderOrganizer']
)
