from setuptools import setup


setup(
    name = "rmz_scaffolder",
    version = "0.1.1",
    author = "Antoine Wendlinger",
    description = ("scaffolder tool"),
    scripts=['bin/rmz_scaffolder'],
    install_requires=['cookiecutter'],
)