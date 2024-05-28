import subprocess
import os
import atexit
from functools import wraps
from pathlib import Path

from history import History


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
def execute(command, history):
    if command.startswith("cd"):
        cd(command)
    elif command.startswith("!"):
        execute_history_item(command, history)
    elif command == "history":
        print(history)
    elif command == "exit":
        exit()
    elif "|" in command:
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


def execute_history_item(command, history):
    value = command.split("!")[-1]
    if not value.isnumeric():
        print(f"{command}: numeric argument required")

    history_command = history.get_item(int(value))
    print(history_command)
    execute(history_command, history)


def run_shell(history):
    try:
        command = input(prompt_text()).rstrip()

        if not command:
            return

        execute(command, history)
    except KeyboardInterrupt:
        print("")


if __name__ == "__main__":
    history_filepath = Path.home() / ".ccsh_history"
    history = History(history_filepath)
    atexit.register(lambda: history.save_to_disk())

    while True:
        run_shell(history)
