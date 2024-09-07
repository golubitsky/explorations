from hashlib import md5


def hash(string):
    return md5(string.encode("utf-8")).hexdigest()


def part_one(data):
    i = 0
    password = []
    while True:
        h = hash(f"{data}{i}")
        if h.startswith("00000"):
            password.append(h[5])
            print(password)

        if len(password) == 8:
            return "".join(password)
        i += 1


def part_two(data):
    i = 0
    password = [None] * 8
    count = 0
    while True:
        h = hash(f"{data}{i}")
        if h.startswith("00000"):
            if h[5] in "01234567":
                index = int(h[5])
                if password[index] is None:
                    password[index] = h[6]
                    print(password)
                    count += 1

        if count == 8:
            return "".join(password)
        i += 1


if __name__ == "__main__":
    print(part_two("cxdnnyjw"))
