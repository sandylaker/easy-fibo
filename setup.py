from typing import List

from setuptools import setup
import pkg_resources


def get_requirements(file: str) -> List[str]:
    with open(file, "r") as f:
        return [str(r) for r in pkg_resources.parse_requirements(f.readlines())]


setup(
    name="easy-fibo",
    version="0.1",
    install_requires=get_requirements("requirements.txt")
)