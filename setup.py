from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."

# Storing the content in Readme file into long_description
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

# Getting the requirements from requirements.txt
with open("requirements.txt", "r") as file:
    requirements = file.readlines()
    requirements = [line.replace("\n", "") for line in requirements]
    requirements.remove("-e .")

setup(
    name="Red Wine Quality Prediction",
    version="0.0.1",
    author="Kishor Reddy",
    author_email="kishorreddy6407@gmail.com",
    description="A Machine Learning model which predicts the wine quality.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kishor2004reddy/RedWineQuality.git",
    packages=find_packages(),
    install_requires=requirements
)
