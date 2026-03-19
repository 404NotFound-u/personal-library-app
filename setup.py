"""
Setup script for Personal Library App
Скрипт настройки сборки пакета проекта
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="personal-library-app",
    version="1.0.0",
    author="404NotFound-u",
    author_email="killer.your.world01@gmail.com",
    description="Веб-приложение для управления личной библиотекой книг",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/404NotFound-u/personal-library-app",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "personal-library=app:app",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["templates/*.html", "static/*/*"],
    },
)
