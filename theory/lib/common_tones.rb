require 'set'
module EngineV1
  extend self

  NOTE_M2_UP = {
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

  def note_interval_away(note:, interval:, direction:)
    case interval
    when 'M2'
      direction == :up ? NOTE_M2_UP.fetch(note) : NOTE_M2_UP.invert.fetch(note)
    when 'P4'
      direction == :up ? NOTE_P4_UP.fetch(note) : NOTE_P4_UP.invert.fetch(note)
    else
      raise "not implemented for #{interval}"
    end
  end

  def pivot_notes(note:, triad:, other_triad:, interval:, direction:)
    other_note = note_interval_away(note: note, interval: interval, direction: direction)

    MAJOR[note].to_set.intersection(MAJOR[other_note].to_set).to_a
  end
end
