from setuptools import setup, find_packages

setup(
  name='mcqgenerator',
  version='0.1.0',
  author='Harsshad Pawar',
  install_requires=['openai','langchain','streamlit','python-dotenv','pyPDF2'],
        packages=find_packages()
  )