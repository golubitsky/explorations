import subprocess
import os

from functools import wraps


def prompt_text():
    return f"ccsh {os.path.basename(os.getcwd())} > "


def exception_handling(function):
    @wraps(function)
    def wrapper(*args):
        try:
            function(*args)
        except Exception as e:
            print(e)

    return wrapper


@exception_handling
def execute(command):
    subprocess.run(command.split())


@exception_handling
def cd(command):
    cmd = command.split()

    if len(cmd) == 1:
        return

    target = cmd[1]

    os.chdir(os.path.join(os.getcwd(), target))


def start_shell():
    while True:
        command = input(prompt_text())

        if command == "exit":
            exit()
        elif command.startswith("cd"):
            cd(command)
        else:
            execute(command)


if __name__ == "__main__":
    start_shell()
