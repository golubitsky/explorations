# frozen_string_literal: true

require 'set'
require 'constants'

module EngineV1
  include Constants
  extend self

  def note_interval_away(note:, interval:, direction:)
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
    case quality
    when :diminished
      third = note_interval_away(note: root, interval: :m3, direction: :up)
      fifth = note_interval_away(note: third, interval: :m3, direction: :up)
    when :minor
      third = note_interval_away(note: root, interval: :m3, direction: :up)
      fifth = note_interval_away(note: third, interval: :M3, direction: :up)
    when :major
      third = note_interval_away(note: root, interval: :M3, direction: :up)
      fifth = note_interval_away(note: third, interval: :m3, direction: :up)
    else
      raise "not implemented for #{quality}"
    end

    [root, third, fifth]
  end

  def enharmonically_simplified_note(note)
    ENHARMONICALLY_SIMPLIFIED[note] || note
  end

  def enharmonically_simplified_chord(chord)
    chord.map { |note| enharmonically_simplified_note(note) }
  end

  def pivot_notes(note:, quality:, other_quality:, interval:, direction:)
    other_note = note_interval_away(note: note, interval: interval, direction: direction)

    chord_tones = enharmonically_simplified_chord(triad(note, quality))
    other_chord_tones = enharmonically_simplified_chord(triad(other_note, other_quality))

    chord_tones.intersection(other_chord_tones).to_a
  end
end
