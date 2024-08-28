import os
from pathlib import Path

from setuptools import setup

name = "m_catz"
version = "0.0.3"
SOURCES_ROOT = Path(__file__).parent.resolve()


def do_setup():
    packages = [x[0].replace("./", "").replace("/", ".") for x in
                filter(lambda x: x[2].__contains__("__init__.py"), os.walk("./"))]
    packages = list(filter(lambda x: "catz.tests" not in x, packages))

    setup(
        name=name,
        email="manhtran40kc@gmail.com",
        version=version,
        packages=packages,
        license="MIT",
        author="manhdoi",
        cmdclass={}
    )


if __name__ == '__main__':
    do_setup()
