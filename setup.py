from setuptools import find_packages, setup

setup(
    name="doc_chatbot",
    version="0.0.1",
    author="Nidhi",
    author_email="your_email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},

)
