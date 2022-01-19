from setuptools import setup, find_packages

URL="https://pottsga.com"

with open ("README.md") as f:
    readme = f.read()

with open ("LICENSE") as f:
    license = f.read()

# Libraries that are required by the application
requires = [
    "pylint",
    "pycodestyle",
    "pytest",
]

setup(
    name="python_boilerplate",
    version="1.0.0",
    description="A sample boilerplate project.",
    long_description=readme,
    author="Greg Potts",
    author_email="pottsga@gmail.com",
    url=URL,
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=requires,
)
