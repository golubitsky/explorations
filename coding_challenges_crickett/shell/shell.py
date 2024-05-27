import subprocess
import os
import atexit

from functools import wraps
from pathlib import Path


class History:
    FILEPATH = Path.home() / ".ccsh_history"

    def __init__(self):
        self._items = self._load_from_disk()

    def append(self, command):
        self._items.append(command)

    def to_stdout(self):
        print("\n".join(self._items))

    def save_to_disk(self):
        with open(History.FILEPATH, "w") as f:
            f.write("\n".join(self._items))

    def _load_from_disk(self):
        try:
            with open(History.FILEPATH) as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []


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


def prompt(history):
    try:
        command = input(prompt_text()).rstrip()

        if not command:
            return

        history.append(command)

        if command.startswith("cd"):
            cd(command)
        elif command == "history":
            history.to_stdout()
        elif command == "exit":
            exit()
        else:
            execute(command)
    except KeyboardInterrupt:
        print("")


if __name__ == "__main__":
    history = History()
    atexit.register(lambda: history.save_to_disk())

    while True:
        prompt(history)
