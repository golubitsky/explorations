import subprocess

PROMPT = "ccsh> "


def start_shell():
    command = input(PROMPT)

    subprocess.run(command)


if __name__ == "__main__":
    start_shell()
