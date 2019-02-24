from setuptools import setup, find_packages

setup(
      name='vocabs',
      version='1.0.0',
      description='A lightweight online dictionary integration to the command line.',
      url='https://github.com/Mckinsey666/Vocab',
      keywords = "cli english words dictionary vocabulary",
      author='Mckinsey666',
      license='MIT',
      packages=find_packages(),
      scripts=["./vocab/vocab"]
    )