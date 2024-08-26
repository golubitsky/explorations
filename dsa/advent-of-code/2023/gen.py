import sys


def create_files(n):
    # Ensure n is formatted as a two-digit string
    n_str = n.zfill(2)

    # Define filenames
    python_file = f"{n_str}.py"
    input_file = f"{n_str}_input.txt"
    sample_file = f"{n_str}_sample.txt"

    # Create and write the Python file
    with open(python_file, "w") as py_file:
        py_file.write(
            f"""
def part_one(data):
    pass

if __name__ == "__main__":
    with open("{n_str}_sample.txt", 'r') as file:
        data = file.readlines()
    print(part_one(data))
"""
        )

    # Create blank text files
    open(input_file, "w").close()
    open(sample_file, "w").close()

    print(f"Files created: {python_file}, {input_file}, {sample_file}")


# Example usage
if __name__ == "__main__":
    create_files(sys.argv[1])
