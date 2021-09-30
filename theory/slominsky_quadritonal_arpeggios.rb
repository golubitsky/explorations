# frozen_string_literal: true

require 'set'

# It is further possible to split the chromatic scale into a diminished triad,
# a minor triad, a major triad, and an augmented triad. These mutually exclusive
# triads can be arranged in the form of Quadritonal Arpeggios.
# - Slominsky's Thesaurus of Scales and Melodic Patterns, page iii

# Quadritonal Arpeggios are a set of 4 mutually exclusive triads.
# This means that none of these triads share the same note.

# In this program, notes are represented by the integers 0 through 11 inclusive.
# For output, notes are translated by index:
NOTE_NAMES = %w[C Db D Eb E F Gb G Ab A Bb B].freeze

ALL_NOTES_IN_OCTAVE = Set.new([*0..11])

# Intervals are measured in half-steps:
TRIAD_INTERVALS_BY_QUALITY = {
  diminished: [0, 3, 6],
  minor: [0, 3, 7],
  major: [0, 4, 7],
  augmented: [0, 4, 8]
}.freeze

QUALITIES = TRIAD_INTERVALS_BY_QUALITY.keys.freeze

def triad(starting_note, quality)
  TRIAD_INTERVALS_BY_QUALITY[quality]
    .map { |interval| starting_note + interval }
    .map { |note| note % 12 }
    .sort
end

def all_possible_triads(quality)
  ALL_NOTES_IN_OCTAVE
    .map { |starting_note| triad(starting_note, quality) }
    .uniq # two inverted augmented chords can contain the same notes
end

def all_possible_triads_by_quality
  QUALITIES.to_h { |quality| [quality, all_possible_triads(quality)] }
end

def all_notes_unique?(*triads)
  triads.flatten.uniq.count == triads.count * 3
end

def quadritonal_arpeggios
  possible_triads = all_possible_triads_by_quality
  quadritonal_arpeggios = []

  possible_triads[:diminished].each do |dim_triad|
    possible_triads[:minor].each do |min_triad|
      possible_triads[:major].each do |maj_triad|
        possible_triads[:augmented].each do |aug_triad|
          next unless all_notes_unique?(dim_triad, min_triad, maj_triad, aug_triad)

          quadritonal_arpeggios << [dim_triad, min_triad, maj_triad, aug_triad]
        end
      end
    end
  end

  quadritonal_arpeggios
end

def as_notes(arpeggio)
  arpeggio.map do |triad|
    triad.map { |note| NOTE_NAMES[note] }.join(' ')
  end
end

quadritonal_arpeggios.each do |arpeggio|
  p as_notes(arpeggio)
end

puts "Found #{quadritonal_arpeggios.count} quadritonal arpeggios, listed above."

# $ ruby slominsky_quadritonal_arpeggios.rb
# ["C Eb Gb", "D G Bb", "E Ab B", "Db F A"]
# ["Db E G", "Eb Ab B", "C F A", "D Gb Bb"]
# ["D F Ab", "C E A", "Db Gb Bb", "Eb G B"]
# ["Eb Gb A", "Db F Bb", "D G B", "C E Ab"]
# ["E G Bb", "D Gb B", "C Eb Ab", "Db F A"]
# ["F Ab B", "C Eb G", "Db E A", "D Gb Bb"]
# ["C Gb A", "Db E Ab", "D F Bb", "Eb G B"]
# ["Db G Bb", "D F A", "Eb Gb B", "C E Ab"]
# ["D Ab B", "Eb Gb Bb", "C E G", "Db F A"]
# ["C Eb A", "E G B", "Db F Ab", "D Gb Bb"]
# ["Db E Bb", "C F Ab", "D Gb A", "Eb G B"]
# ["D F B", "Db Gb A", "Eb G Bb", "C E Ab"]
# Found 12 quadritonal arpeggios, listed above.
