import subprocess

PROMPT = "ccsh> "


def start_shell():
    while True:
        command = input(PROMPT)

        if command == "exit":
            exit()

        subprocess.run(command)


if __name__ == "__main__":
    start_shell()
