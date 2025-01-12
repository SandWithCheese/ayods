from setuptools import setup, find_packages

setup(
    name="ayods",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"ayods": ["templates/*.ipynb"]},
    install_requires=["questionary==2.1.0"],
    entry_points={
        "console_scripts": [
            "ayods=ayods.main:main",
        ],
    },
    description="Python CLI tool for initializing data science projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ahmad Naufal Ramadan",
    author_email="naufalahmad022@gmail.com",
    url="https://github.com/SandWithCheese/ayods",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
