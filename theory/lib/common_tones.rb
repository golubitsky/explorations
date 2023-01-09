# frozen_string_literal: true

require 'set'
require 'constants'

module EngineV1
  include Constants
  extend self

  def note_interval_away(note:, interval:, direction:)
    return note if interval == :P1

    if INVERSE_INTERVAL[interval]
      interval = INVERSE_INTERVAL[interval]
      direction = %i[up down].find { |x| x != direction }
    end

    notes_up_interval = {
      m2: NOTE_MINOR2_UP,
      M2: NOTE_MAJOR2_UP,
      m3: NOTE_MINOR3_UP,
      M3: NOTE_MAJOR3_UP,
      P4: NOTE_P4_UP,
      P5: NOTE_P5_UP,
    }.fetch(interval)

    notes = direction == :up ? notes_up_interval : notes_up_interval.invert

    raise "not implemented: #{interval} #{direction} from #{note}" unless notes[note]

    notes[note]
  end

  def triad(root, quality)
    intervals_by_quality = {
      diminished: %i[m3 m3],
      minor: %i[m3 M3],
      major: %i[M3 m3],
      augmented: %i[M3 M3],
    }
    intervals = intervals_by_quality[quality]
    raise "triad not implemented for #{quality}" unless intervals

    intervals.reduce([root]) do |chord, interval|
      [
        *chord,
        note_interval_away(
          note: chord.last,
          interval: interval,
          direction: :up
        ),
      ]
    end
  end

  def enharmonically_equivalent_notes(chord, other_chord)
    enharmonically_simplified_other_chord =
      other_chord.map { |note| ENHARMONICALLY_SIMPLIFIED[note] || note }

    chord.select do |note|
      other_chord.include?(note) ||
        enharmonically_simplified_other_chord.include?(note)
    end
  end

  def pivot_notes(note:, quality:, other_quality:, interval:, direction:)
    other_note = note_interval_away(note: note, interval: interval, direction: direction)

    chord = triad(note, quality)
    other_chord = triad(other_note, other_quality)

    enharmonically_equivalent_notes(chord, other_chord)
  end

  def pivot_chords(notes)
    all_chords = NOTE_MINOR2_UP.keys.flat_map do |note|
      QUALITIES.map { |quality| triad(note, quality) }
    end

    all_chords.select { |chord| notes.all? { |note| chord.include?(note) } }
  end
end
