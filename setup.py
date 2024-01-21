from setuptools import setup, find_packages

setup(
  name='mcqgenerator',
  version='0.1.0',
  author='Harsshad Pawar',
  author_email='pawar.harshad186@gmail.com',
  install_requires=['openai','langchain','streamlit','python-dotenv','pyPDF2'],
        packages=find_packages()
  )