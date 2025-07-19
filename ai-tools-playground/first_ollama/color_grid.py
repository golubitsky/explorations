from colorama import Fore, Back, Style, init

# Supported colors mapped to colorama background codes
COLOR_MAP = {
    "black": Back.BLACK,
    "red": Back.RED,
    "green": Back.GREEN,
    "yellow": Back.YELLOW,
    "blue": Back.BLUE,
    "magenta": Back.MAGENTA,
    "cyan": Back.CYAN,
    "white": Back.WHITE,
}


class ColorGrid:
    def __init__(self, size=10, default_color="white"):
        self.size = size
        self.grid = [[default_color for _ in range(size)] for _ in range(size)]

    def set_cell(self, x, y, color):
        if color not in COLOR_MAP:
            raise ValueError(f"Unsupported color: {color}")
        if 0 <= x < self.size and 0 <= y < self.size:
            self.grid[y][x] = color
        else:
            raise IndexError("Cell coordinates out of bounds")

    def print(self):
        for row in self.grid:
            for color in row:
                # Print a colored block character (2-wide for better visibility)
                print(COLOR_MAP[color] + "  ", end="")
            print(Style.RESET_ALL)  # Reset at end of row


# Example usage
if __name__ == "__main__":
    grid = ColorGrid()
    grid.set_cell(0, 0, "red")
    grid.set_cell(1, 1, "green")
    grid.set_cell(2, 2, "blue")
    grid.print_grid()
