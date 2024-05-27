import subprocess

PROMPT = "ccsh> "


def start_shell():
    while True:
        command = input(PROMPT)

        if command == "exit":
            exit()

        try:
            subprocess.run(command.split(), check=True)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    start_shell()
