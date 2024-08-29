from collections import namedtuple

BROADCASTER = "broadcaster"
OUTPUT = "output"
BUTTON = "button"
RX = "rx"

FLIP_FLOP = "flip"
CONJUNCTION = "conjunction"

DESTINATIONS = "destinations"

LOW = "low"
HIGH = "hi"

ON = "on"
OFF = "off"

TYPE = "type"
STATE = "state"


Pulse = namedtuple("Pulse", "source destination type")


def parsed_modules(data):
    modules = {}

    for line in data:
        name, destinations = [x.strip() for x in line.split("->")]
        if name == BROADCASTER:
            module_type = BROADCASTER
        else:
            module_type, name = name[0], name[1:]
        if module_type == "%":
            module_type = FLIP_FLOP
        elif module_type == "&":
            module_type = CONJUNCTION
        else:
            if module_type != BROADCASTER:
                print("unknown type")
                exit()

        modules[name] = {
            TYPE: module_type,
            DESTINATIONS: [x.strip() for x in destinations.split(",")],
        }

    modules[BUTTON] = {
        TYPE: BUTTON,
        DESTINATIONS: [BROADCASTER],
    }

    modules[OUTPUT] = {
        TYPE: OUTPUT,
        DESTINATIONS: [],
    }

    modules[RX] = {
        TYPE: OUTPUT,
        DESTINATIONS: [],
    }

    return modules


def next_flip_state(flip=None):
    if flip is None or flip == ON:
        return OFF
    else:
        return ON


def next_flip_signal_type(module):
    if module[STATE] == ON:
        return HIGH
    else:
        return LOW


def next_conjunction_signal_type(module):
    if all(pulse_type == HIGH for pulse_type in module[STATE].values()):
        return LOW
    else:
        return HIGH


def set_initial_module_state(modules):
    for name in modules:
        module = modules[name]
        if module[TYPE] == FLIP_FLOP:
            module[STATE] = next_flip_state()
        if module[TYPE] == CONJUNCTION:
            module[STATE] = {}

    for name in modules:
        module = modules[name]
        for dest_name in module[DESTINATIONS]:
            dest_module = modules[dest_name]
            if dest_module[TYPE] == CONJUNCTION:
                dest_module[STATE][name] = LOW


def emitted_pulses(pulse, modules):
    pulses = []

    if pulse.destination == BROADCASTER:
        for destination in modules[BROADCASTER][DESTINATIONS]:
            pulses.append(Pulse(BROADCASTER, destination, pulse.type))
    else:
        module = modules[pulse.destination]

        if module[TYPE] == FLIP_FLOP:
            if pulse.type == LOW:
                module[STATE] = next_flip_state(module[STATE])
                sig_type = next_flip_signal_type(module)

                for destination in module[DESTINATIONS]:
                    pulses.append(
                        Pulse(
                            pulse.destination,
                            destination,
                            sig_type,
                        )
                    )

        if module[TYPE] == CONJUNCTION:
            module[STATE][pulse.source] = pulse.type
            sig_type = next_conjunction_signal_type(module)

            for destination in module[DESTINATIONS]:
                pulses.append(
                    Pulse(
                        pulse.destination,
                        destination,
                        sig_type,
                    )
                )

    return pulses


def debug_print(s):
    return
    print(s)


def push_button(modules):
    debug_print("pushing button")
    pulses = [Pulse(BUTTON, BROADCASTER, LOW)]

    pulse_count = {LOW: 0, HIGH: 0}
    emitted_high_to_dh = {}
    while pulses:
        new_pulses = []
        for pulse in pulses:
            for emitted in emitted_pulses(pulse, modules):
                new_pulses.append(emitted)
                debug_print(f"{emitted.source} -{emitted.type}-> {emitted.destination}")
                pulse_count[emitted.type] += 1
                # dh -> rx
                # xm -> dh
                # dr -> dh
                # nh -> dh
                if emitted.type == HIGH and emitted.source in ["xm", "dr", "nh", "tr"]:
                    emitted_high_to_dh[emitted.source] = True
        pulses = new_pulses

    return pulse_count, emitted_high_to_dh


def part_one(data):
    modules = parsed_modules(data)
    set_initial_module_state(modules)

    n_button_presses = 1000
    pulse_count = {LOW: n_button_presses, HIGH: 0}
    for _ in range(n_button_presses):
        counts, _ = push_button(modules)
        for sig_type in counts:
            pulse_count[sig_type] += counts[sig_type]
        debug_print("")

    print(pulse_count[LOW] * pulse_count[HIGH])


def part_two(data):
    modules = parsed_modules(data)
    set_initial_module_state(modules)

    # count = 0
    # while True:
    #     _, signal_sent = push_button(modules)
    #     count += 1
    #     count_by_source = {"xm": 3761, "dr": 3797, "nh": 3889, "tr": 3739}
    #     for source in count_by_source:
    #         if source in signal_sent:
    #             print(source, count % count_by_source[source])
    print(3761 * 3797 * 3889 * 3739)


if __name__ == "__main__":
    with open("day_20_input.txt", "r") as file:
        data = file.readlines()
    part_two(data)
