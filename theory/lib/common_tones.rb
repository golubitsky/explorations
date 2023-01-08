require 'set'
module EngineV1
  extend self

  NOTE_MAJOR2_UP = {
    'A' => 'B',
    'A#' => 'B#',
    'Bb' => 'C',
    'B' => 'C#',
    'C' => 'D',
    'C#' => 'D#',
    'Db' => 'Eb',
    'D' => 'E',
    'D#' => 'E#',
    'Eb' => 'F',
    'E' => 'F#',
    'F' => 'G',
    'F#' => 'G#',
    'Gb' => 'Ab',
    'G' => 'A',
    'G#' => 'A#',
    'Ab' => 'Bb',
  }

  NOTE_MINOR3_UP = {
    'A' => 'C',
    'A#' => 'C#',
    'Bb' => 'Db',
    'B' => 'D',
    'C' => 'Eb',
    'C#' => 'E',
    'Db' => 'Fb',
    'D' => 'F',
    'D#' => 'F#',
    'Eb' => 'Gb',
    'E' => 'G',
    'F' => 'Ab',
    'F#' => 'A',
    'Gb' => 'Bbb',
    'G' => 'Bb',
    'G#' => 'B',
    'Ab' => 'Cb',
  }

  NOTE_MAJOR3_UP = {
    'A' => 'C#',
    'A#' => 'C##',
    'Bb' => 'D',
    'B' => 'D#',
    'Cb' => 'Eb',
    'C' => 'E',
    'C#' => 'E#',
    'Db' => 'F',
    'D' => 'F#',
    'D#' => 'F##',
    'Eb' => 'G',
    'E' => 'G#',
    'F' => 'A',
    'F#' => 'A#',
    'Gb' => 'Bb',
    'G' => 'B',
    'G#' => 'B#',
    'Ab' => 'C',
  }

  NOTE_P4_UP = {
    'A' => 'D',
    'A#' => 'D#',
    'Bb' => 'Eb',
    'B' => 'E',
    'C' => 'F',
    'C#' => 'F#',
    'Db' => 'Gb',
    'D' => 'G',
    'D#' => 'G#',
    'Eb' => 'Ab',
    'E' => 'A',
    'F' => 'Bb',
    'F#' => 'B',
    'Gb' => 'Cb',
    'G' => 'C',
    'G#' => 'C#',
    'Ab' => 'Db',
  }

  NOTE_P5_UP = {
    'A' => 'E',
    'A#' => 'E#',
    'Bb' => 'F',
    'B' => 'F#',
    'C' => 'G',
    'C#' => 'G#',
    'Db' => 'Ab',
    'D' => 'A',
    'D#' => 'A#',
    'Eb' => 'Bb',
    'E' => 'B',
    'F' => 'C',
    'F#' => 'C#',
    'Gb' => 'Db',
    'G' => 'D',
    'G#' => 'D#',
    'Ab' => 'D#',
  }

  def note_interval_away(note:, interval:, direction:)
    notes_up_interval = {
      M2: NOTE_MAJOR2_UP,
      m3: NOTE_MINOR3_UP,
      M3: NOTE_MAJOR3_UP,
      P4: NOTE_P4_UP,
      P5: NOTE_P5_UP,
    }.fetch(interval)

    notes = direction == :up ? notes_up_interval : notes_up_interval.invert

    notes.fetch(note)
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

  def pivot_notes(note:, quality:, other_quality:, interval:, direction:)
    other_note = note_interval_away(note: note, interval: interval, direction: direction)

    chord_tones = triad(note, quality)
    other_chord_tones = triad(other_note, other_quality)

    chord_tones.intersection(other_chord_tones).to_a
  end
end
