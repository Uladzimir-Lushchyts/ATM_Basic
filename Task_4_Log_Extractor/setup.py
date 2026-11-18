from setuptools import setup, find_packages

setup(
    name="log_extractor",
    version="0.1.0",
    description="Extracts sessions from log files",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "log-extractor=log_extractor.main:main",
        ],
    },
)
