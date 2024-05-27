import subprocess
import os

from functools import wraps

PROMPT = "ccsh> "


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
    subprocess.run(command)


@exception_handling
def cd(command):
    if len(command) == 1:
        return

    target = command[1]

    os.chdir(os.path.join(os.getcwd(), target))


def start_shell():
    while True:
        command = input(PROMPT).split()

        if command[0] == "exit":
            exit()
        elif command[0] == "cd":
            cd(command)
        else:
            execute(command)


if __name__ == "__main__":
    start_shell()
