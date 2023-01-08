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
  }

  NOTE_MAJOR3_UP = {
    'A' => 'C#',
    'A#' => 'C##',
    'Bb' => 'D',
    'B' => 'D#',
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
  }

  MAJOR = {
    'C' => %w[C E G],
    'C#' => %w[C# E# G#],
    'Db' => %w[Db F Ab],
    'D' => %w[D F# A],
    'D#' => %w[D# F## A#],
    'Eb' => %w[Eb G Bb],
    'E' => %w[E G# B],
    'F' => %w[F A C],
    'F#' => %w[F# A# C#],
    'Gb' => %w[Gb Bb Db],
    'G' => %w[G B D],
    'G#' => %w[G# B# D#],
    'Ab' => %w[Ab C Eb],
    'A' => %w[A C# E],
    'A#' => %w[A# C## E#],
    'Bb' => %w[Bb D F],
    'B' => %w[B D# F#],
  }

  MINOR = {
    'C' => %w[C Eb G],
    'C#' => %w[C# E G#],
    'Db' => %w[Db Fb Ab],
    'D' => %w[D F A],
    'D#' => %w[D# F# A#],
    'Eb' => %w[Eb Gb Bb],
    'E' => %w[E G B],
    'F' => %w[F Ab C],
    'F#' => %w[F# A C#],
    'Gb' => %w[Gb Bbb Db],
    'G' => %w[G Bb D],
    'G#' => %w[G# B D#],
    'Ab' => %w[Ab Cb Eb],
    'A' => %w[A C E],
    'A#' => %w[A# C# E#],
    'Bb' => %w[Bb Db F],
    'B' => %w[B D F#],
  }

  DIMINISHED = {
    'C' => %w[C Eb Gb],
    'C#' => %w[C# E G],
    'Db' => %w[Db Fb Abb],
    'D' => %w[D F Ab],
    'D#' => %w[D# F# A],
    'Eb' => %w[Eb Gb Bbb],
    'E' => %w[E G Bb],
    'F' => %w[F Ab Cb],
    'F#' => %w[F# A C],
    'Gb' => %w[Gb Bbb Dbb],
    'G' => %w[G Bb Db],
    'G#' => %w[G# B D],
    'Ab' => %w[Ab Cb Ebb],
    'A' => %w[A C Eb],
    'A#' => %w[A# C# E],
    'Bb' => %w[Bb Db Fb],
    'B' => %w[B D F],
  }

  def note_interval_away(note:, interval:, direction:)
    case interval
    when 'M2'
      direction == :up ? NOTE_MAJOR2_UP.fetch(note) : NOTE_MAJOR2_UP.invert.fetch(note)
    when 'm3'
      direction == :up ? NOTE_MINOR3_UP.fetch(note) : NOTE_MINOR3_UP.invert.fetch(note)
    when 'M3'
      direction == :up ? NOTE_MAJOR3_UP.fetch(note) : NOTE_MAJOR3_UP.invert.fetch(note)
    when 'P4'
      direction == :up ? NOTE_P4_UP.fetch(note) : NOTE_P4_UP.invert.fetch(note)
    when 'P5'
      direction == :up ? NOTE_P5_UP.fetch(note) : NOTE_P5_UP.invert.fetch(note)
    else
      raise "not implemented for #{interval}"
    end
  end

  def pivot_notes(note:, triad:, other_triad:, interval:, direction:)
    other_note = note_interval_away(note: note, interval: interval, direction: direction)

    chord_by_quality = {
      major: MAJOR,
      minor: MINOR,
      diminished: DIMINISHED,
    }

    chord_tones = chord_by_quality.fetch(triad)[note].to_set
    other_chord_tones = chord_by_quality.fetch(other_triad)[other_note].to_set

    chord_tones.intersection(other_chord_tones).to_a
  end
end
