from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="zephyr_behave",
    version="1.1.4",
    description="Generate Zephyr compatible file for uploading to Zephyr",
    long_description="Test results are recorded, and a Zephyr compatible json file is generated. A compressed and uncompressed file is created",
    url="https://github.com/KotieSmit/zephyr_behave",
    author="Kotie Smit",
    author_email="",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="bdd behave automation json Zephyr",
    packages=find_packages(),
    install_requires=[
        "behave2cucumberZephyr"
    ],
    extras_require={},
    data_files=[],
    py_modules=[],
)
