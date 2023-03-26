import json
import sys


def main():
    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as file:
            json.loads(file.read())
        print(f"{file_name} is valid JSON")
        exit(0)
    except json.JSONDecodeError:
        print(f"{file_name} is invalid JSON")
        exit(1)


if __name__ == "__main__":
    main()
