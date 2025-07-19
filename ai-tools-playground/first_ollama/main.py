import ast
import os
from color_grid import ColorGrid, COLOR_MAP
from ollama_client import ask_ollama


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def log(message, level="INFO"):
    if level == "ERROR":
        file_name = "error.log"
    elif level == "INFO":
        file_name = "info.log"
    with open(file_name, "a") as f:
        f.write(message + "\n")


# TODO: cleaner separation of concerns
def update_grid_with_ollama_response(grid, response):
    log(response)

    for line in response.lower().splitlines():
        if "set" in line and "to" in line:
            try:
                _, coords, _, color = line.split()
                x, y = ast.literal_eval(coords)
                grid.set_cell(x, y, color)
            except Exception:
                log(f"Malformed line: {line}\n", level="ERROR")
                pass  # ignore malformed lines


def main():
    grid = ColorGrid()

    while True:
        base_prompt = open("prompt.txt", "r").read()
        clear_screen()
        grid.print()
        print("\nType a prompt or press Enter to skip (type 'quit' to exit):")
        user_input = input("> ").strip()

        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            break

        log(user_input)

        full_prompt = (
            f"{base_prompt}\n\n"
            f"List of valid colors: {list(COLOR_MAP.keys())}\n"
            f"User instruction: {user_input}\n"
            f"Current grid: {grid.grid}"
        )
        response = ask_ollama(full_prompt)
        update_grid_with_ollama_response(grid, response)


if __name__ == "__main__":
    main()
