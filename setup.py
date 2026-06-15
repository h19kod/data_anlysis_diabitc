"""
Diabetes Prediction System - Setup File
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="diabetes-prediction",
    version="1.0.0",
    author="H19KOD",
    author_email="user@example.com",
    description="A comprehensive diabetes prediction system using Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h19kod/data_anlysis_diabitc",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "diabetes-dashboard=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
