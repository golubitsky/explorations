class History:
    def __init__(self, filepath):
        self._filepath = filepath
        self._items = self._load_from_disk()

    def __str__(self):
        return "\n".join(self._items)

    def append(self, command):
        self._items.append(command)

    def save_to_disk(self):
        with open(self._filepath, "w") as f:
            f.write(self.__str__())

    def _load_from_disk(self):
        try:
            with open(self._filepath) as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []
