def box_number(label):
    value = 0
    for char in label:
        if char in {"\n"}:
            continue

        value += ord(char)
        value *= 17
        value %= 256
    return value


def part_one(init_sequence):
    return sum([box_number(word) for word in init_sequence])


def print_boxes(boxes):
    for index, box in enumerate(boxes):
        if not box:
            continue
        contents = " ".join([f'[{l['label']} {l['focal_length']}]' for l in box])
        print(f'Box {index}:', contents)


def focusing_power(boxes):
    total = 0
    for box_index, box in enumerate(boxes):
        if not box:
            continue

        for lens_index, lens in enumerate(box):
            total += (box_index + 1) * (lens_index + 1) * int(lens['focal_length'])
    
    return total

def part_two(init_sequence):
    boxes = [None] * 256
    for index in range(len(boxes)):
        boxes[index] = []

    for step in init_sequence:
        if "=" in step:
            label, focal_length = step.split("=")
            box = boxes[box_number(label)]
            item = next((x for x in box if x['label'] == label), None)
            if item is not None:
                item['focal_length'] = focal_length
            else:
                boxes[box_number(label)].append(
                    {"label": label, "focal_length": focal_length}
                )
        elif "-" in step:
            label, _ = step.split("-")
            box = boxes[box_number(label)]
            item = next((x for x in box if x['label'] == label), None)
            if item is not None:
                box.remove(item)
        else:
            raise "unknown step"
    print(focusing_power(boxes))


if __name__ == "__main__":
    with open("day_15_input.txt", "r") as file:
        data = file.read().split(",")
    # print(part_one(data))
    part_two(data)
    
