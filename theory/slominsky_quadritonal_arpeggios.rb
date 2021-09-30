# frozen_string_literal: true

require 'set'

# It is further possible to split the chromatic scale into a diminished triad,
# a minor triad, a major triad, and an augmented triad. These mutually exclusive
# triads can be arranged in the form of Quadritonal Arpeggios.
# - Slominsky's Thesaurus of Scales and Melodic Patterns, page iii

# Quadritonal Arpeggios are a set of 4 mutually exclusive triads.
# This means that none of these triads share the same note.

# diminished  0 +3 +6
# minor       0 +3 +7
# major       0 +4 +7
# augmented   0 +4 +8

# 0 1 2 3 4 5
# 0   2   4
#   1   3   5

# simple case: universe of starting notes without chord inversions
# possible starting notes
# dim [0..5] # total: 6
# min [0..4] # total: 5
# maj [0..4] # total: 5
# aug [0..3] # total: 4

# notes are represented by integers [0..11]
# iterate over triad types
#   iterate over each available starting position (based on unused notes)

TRIAD_INTERVALS_BY_QUALITY = {
  dim: [0, 3, 6],
  min: [0, 3, 7],
  maj: [0, 4, 7],
  aug: [0, 4, 8]
}

POSSIBLE_STARTING_NOTES_BY_QUALITY = {
  dim: [*0..5],
  min: [*0..4],
  maj: [*0..4],
  aug: [*0..3]
}

ALL_NOTES_IN_OCTAVE = Set.new([0..11])

QUALITIES = TRIAD_INTERVALS_BY_QUALITY.keys.freeze

def triad(starting_note, triad_intervals)
  triad_intervals.map { |interval| starting_note + interval }
end

def eligible_triad?(triad, quadritonal_arpeggio)
  quadritonal_arpeggio.flatten.each do |note_in_arpeggio|
    return false if triad.include?(note_in_arpeggio)
  end

  true
end

def debug(level, string)
  puts "level #{level} #{string}"
end

# naive means: do not consider any chord inversions
def quadritonal_arpeggio_naively(qualities = QUALITIES, quadritonal_arpeggio = [], level = 0)
  debug(level, "qualities: #{qualities}")
  return quadritonal_arpeggio if qualities.empty?

  qualities.each do |quality|
    POSSIBLE_STARTING_NOTES_BY_QUALITY[quality].each do |starting_note|
      possible_triad = triad(starting_note, TRIAD_INTERVALS_BY_QUALITY[quality])
      debug(level, "trying #{possible_triad}")

      if eligible_triad?(possible_triad, quadritonal_arpeggio)
        quadritonal_arpeggio << possible_triad

        remaining_qualities = qualities.reject { |q| q == quality }
        next_level_arpeggio = quadritonal_arpeggio_naively(remaining_qualities, quadritonal_arpeggio, level + 1)

        debug(level, ">>>next_level_arpeggio #{next_level_arpeggio}")
      else
        debug(level, "ineligible #{possible_triad}")
        next
      end
    end
  end

  quadritonal_arpeggio
end

# p QUALITIES
quadritonal_arpeggio_naively
p 'hi'

# TODO: above is a failed attempt.
# 1. inversions -- obviously need to consider (i.e. fix the naive aspect)
# 2. try it from another angle: build all the combinations of 4 random 3-note combos in 12 notes,
# -  and then select those that are entirely composed of one of the _actual_ triads
# - ^^^ this seems like the way to go
