from setuptools import setup, find_packages


setup(
    name='PuncPy',
    version='0.1',
    description='Punctuation Library',
    author='Mark Brownsword',
    author_email='markbrownsword@gmail.com',
    url='https://github.com/markbrownsword/punc-py',
    packages=find_packages(),
    install_requires=[
        'nltk'
    ]
)
