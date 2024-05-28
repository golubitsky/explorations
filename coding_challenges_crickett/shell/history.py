import readline


class History:
    def __init__(self, filepath):
        self._filepath = filepath

        try:
            readline.read_history_file(self._filepath)
        except FileNotFoundError:
            pass

    def __str__(self):
        print(readline.get_current_history_length())

        def single_item(i):
            # readline uses 1-indexing
            number = str((i + 1)).rjust(5)
            command = readline.get_history_item(i + 1)

            return "  ".join([number, command])

        return "\n".join(
            [single_item(i) for i in range(readline.get_current_history_length())]
        )

    def save_to_disk(self):
        readline.write_history_file(self._filepath)
