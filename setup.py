from setuptools import find_packages,setup

setup (
    name='mcqgenerator',
    version='0.0.1',
    author='Kartheek Challa',
    author_email='challakartheek@gmail.com',
    install_requires=['openai','langchain','streamlit','python-dotenv','pypdf2','pandas','langchain-community'],
    packages=find_packages()
)