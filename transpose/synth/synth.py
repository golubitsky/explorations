import math
import random

from synthesizer import Player, Synthesizer, Waveform

A_440 = 440

MAJOR = [0, 4, 7]
MINOR = [0, 3, 7]
DIM = [0, 3, 6]
DOM = [0, 4, 7, 10]
SHARP_ELEVEN = [0, 4, 7, 11, 14, 18]
THIRTEEN = [0, 4, 7, 10, 14, 21]


def frequency(half_steps_from_a_440):
    return math.pow(2, half_steps_from_a_440/12) * A_440


def frequencies(half_steps_away):
    return [frequency(half_steps_away) for half_steps_away in half_steps_away]


def random_transpose(frequencies):
    r = random.uniform(0.5, 1)
    return [f * r for f in frequencies]


def play(chord):
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.4, use_osc2=False)
    player.play_wave(synthesizer.generate_chord(chord, 1))


if __name__ == "__main__":
    chords = [SHARP_ELEVEN, MAJOR, MINOR, DIM, DOM, THIRTEEN]
    random.shuffle(chords)
    for chord_type in chords:
        play(random_transpose(frequencies(chord_type)))
