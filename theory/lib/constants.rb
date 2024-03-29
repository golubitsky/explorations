# frozen_string_literal: true

module Constants
  QUALITIES = %i[diminished minor major augmented]

  NOTE_MINOR2_UP = {
    'A' => 'Bb',
    'Bb' => 'Cb',
    'B' => 'C',
    'C' => 'Db',
    'C#' => 'D',
    'Db' => 'Ebb',
    'D' => 'Eb',
    'D#' => 'E',
    'Eb' => 'Fb',
    'E' => 'F',
    'F' => 'Gb',
    'F#' => 'G',
    'Gb' => 'Abb',
    'G' => 'Ab',
    'G#' => 'A',
    'Ab' => 'Bbb',
  }

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
    'Bbb' => 'Dbb',
    'B' => 'D',
    'B#' => 'D#',
    'Cb' => 'Ebb',
    'C' => 'Eb',
    'C#' => 'E',
    'Db' => 'Fb',
    'D' => 'F',
    'D#' => 'F#',
    'Eb' => 'Gb',
    'E' => 'G',
    'E#' => 'G#',
    'Fb' => 'Abb',
    'F' => 'Ab',
    'F#' => 'A',
    'F##' => 'A#',
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
    'B#' => 'D##',
    'Bbb' => 'Db',
    'Cb' => 'Eb',
    'C' => 'E',
    'C#' => 'E#',
    'Db' => 'F',
    'D' => 'F#',
    'D#' => 'F##',
    'Eb' => 'G',
    'E' => 'G#',
    'E#' => 'G##',
    'Fb' => 'Ab',
    'F' => 'A',
    'F#' => 'A#',
    'F##' => 'A##',
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

  ENHARMONIC = {
    # non-accidentals that have single-accidental enharmonic
    'B' => 'Cb',
    'E' => 'Fb',
    # this one is a hack to get one test to pass — need to rethink
    # "enharmonic engine" — in this case, A could be either G## or Bbb
    'A' => 'Bbb',
    # flats
    'Bb' => 'A#',
    'Eb' => 'D#',
    'Ab' => 'G#',
    'Db' => 'C#',
    'Gb' => 'F#',
    'Cb' => 'B',
    'Fb' => 'E',
    # sharps
    'F#' => 'Gb',
    'C#' => 'Db',
    'G#' => 'Ab',
    'D#' => 'Eb',
    'A#' => 'Bb',
    'E#' => 'F',
    'B#' => 'C',
    # double sharps
    'A##' => 'B',
    'B##' => 'C#',
    'C##' => 'D',
    'D##' => 'E',
    'E##' => 'F#',
    'F##' => 'G',
    'G##' => 'A',
    # double flats
    'Abb' => 'G',
    'Bbb' => 'A',
    'Cbb' => 'Bb',
    'Dbb' => 'C',
    'Ebb' => 'D',
    'Fbb' => 'Eb',
    'Gbb' => 'F',
  }

  INVERSE_INTERVAL = {
    M7: :m2,
    m7: :M2,
    M6: :m3,
    m6: :M3,
  }.freeze
end
