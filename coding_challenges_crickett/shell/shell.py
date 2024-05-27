import subprocess
import os

from functools import wraps


def prompt_text():
    return f"ccsh {os.path.basename(os.getcwd())} > "


def command_exception_handling(function):
    @wraps(function)
    def wrapper(*args):
        try:
            function(*args)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            pass

    return wrapper


@command_exception_handling
def execute(command):
    if "|" in command:
        stdin = None
        for command in command.split("|"):
            completed_process = subprocess.run(
                command.split(), input=stdin, stdout=subprocess.PIPE
            )
            stdin = completed_process.stdout

        print(completed_process.stdout.decode("utf-8"))
    else:
        subprocess.run(command.split())


@command_exception_handling
def cd(command):
    cmd = command.split()

    if len(cmd) == 1:
        return

    target = cmd[1]

    os.chdir(os.path.join(os.getcwd(), target))


def prompt():
    try:
        command = input(prompt_text())

        if command == "exit":
            exit()
        elif command.startswith("cd"):
            cd(command)
        else:
            execute(command)
    except KeyboardInterrupt:
        print("")


if __name__ == "__main__":
    while True:
        prompt()
