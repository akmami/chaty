from setuptools import setup, find_packages

setup(
    name="chaty",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
    ],
    author="Akmuhammet Ashyralyyev",
    author_email="akmuhammet99@gmail.com",
    description="A library to interact with ChatGPT",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/akmami/chaty",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
