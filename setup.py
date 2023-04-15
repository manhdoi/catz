import glob
from pathlib import Path

from setuptools import setup, Command
import logging

import os

name = "catz"
SOURCES_ROOT = Path(__file__).parent.resolve()


def print_curry_functions(n: int) -> str:
    ret = f"""def curry{n}(func):"""

    def print_body(res: str, i: int, tab_num: int):
        tabs = "\t" * tab_num
        res = f"""{res}\n{tabs}def wrap{i}(p{i}):"""
        if i < n:
            res = print_body(res, i + 1, tab_num + 1)
        else:
            return_str = ", ".join(map(lambda x: f"p{x + 1}", range(n)))
            res = f"""{res}\n{tabs}\treturn func({return_str})"""
        res = f"""{res}\n{tabs}return wrap{i}"""
        return res

    ret = print_body(ret, 1, 1)
    return ret


class GenerateCurryFunctions(Command):
    user_options: list[str] = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        with open("./catz/common/functions.py", "w+") as f:
            for i in range(50):
                code_string = print_curry_functions(i + 2)
                f.writelines(code_string)
                f.write("\n")


class CleanCommand(Command):
    user_options: list[str] = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    @staticmethod
    def rm_all_files(file) -> None:
        files = glob.glob(file)
        stack = files
        files_sorted = []

        def rec(stk):
            while stk:
                f = stk.pop()
                fs = glob.glob(f"{f}/*", recursive=True)
                for i in fs:
                    stk.append(i)
                    rec(stk)
                files_sorted.append(f)
            return

        rec(stack)

        for x in files_sorted:
            try:
                logging.info(f"Removing {x}")
                if os.path.isfile(x):
                    os.remove(x)
                else:
                    os.rmdir(x)
            except Exception as e:
                logging.warning(f"Error when removing {x}")

    def run(self) -> None:
        os.chdir(str(SOURCES_ROOT))
        self.rm_all_files("./build/*")
        self.rm_all_files("./build")
        self.rm_all_files("./.pytest_cache/*")
        self.rm_all_files("./*.egg-info/*")
        self.rm_all_files("./*.egg-info")
        self.rm_all_files("./dist/*")
        self.rm_all_files("./dist")
        self.rm_all_files('./**/__pycache__/*')
        self.rm_all_files('./**/*.pyc')


def do_setup():
    packages = [x[0].replace("./", "").replace("/", ".") for x in
                filter(lambda x: x[2].__contains__("__init__.py"), os.walk("./"))]
    packages = list(filter(lambda x: "catz.tests" not in x, packages))

    with open("version.txt", "r") as f:
        version = f.read().strip()

        setup(
            name=name,
            email="manhtran40kc@gmail.com",
            version=version,
            packages=packages,
            license="",
            author="manhdoi",
            cmdclass={
                'clean': CleanCommand,
                "g_curry": GenerateCurryFunctions
            }
        )


if __name__ == '__main__':
    do_setup()
