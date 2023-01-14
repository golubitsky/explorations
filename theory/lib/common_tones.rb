# frozen_string_literal: true

require 'set'
require 'constants'
require 'engine_v2'
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
    enharmonic_other_chord =
      other_chord.map { |note| ENHARMONIC[note] }

    chord.select do |note|
      other_chord.include?(note) ||
        enharmonic_other_chord.include?(note)
    end
  end

  def pivot_notes(note:, quality:, other_quality:, interval:, direction:)
    other_note = note_interval_away(note: note, interval: interval, direction: direction)

    chord = triad(note, quality)
    other_chord = triad(other_note, other_quality)

    enharmonically_equivalent_notes(chord, other_chord)
  end

  def accidental?(note)
    note.include?('b') || note.include?('#')
  end

  def simpler_enharmonic?(note:, other_note:)
    note.scan(/b|#/).count < other_note.scan(/b|#/).count
  end

  def enharmonic_chord(chord)
    chord.map { |note| ENHARMONIC[note] }
  end

  def chord_includes_note?(chord, note)
    (chord + enharmonic_chord(chord)).include?(note)
  end

  def filtered_with_enharmonic_preference_for_requested_notes(chords:, target_notes:)
    chords.reject do |chord|
      enharmonic_chord = enharmonic_chord(chord)

      next unless chords.include?(enharmonic_chord)

      target_note_count_in_chord =
        chord.count { |note| target_notes.include?(note) }
      target_note_count_in_enharmonic_chord =
        enharmonic_chord.count { |note| target_notes.include?(note) }

      target_note_count_in_enharmonic_chord > target_note_count_in_chord
    end
  end

  def pivot_chords(notes)
    all_chords = NOTE_MINOR2_UP.keys.flat_map do |note|
      chords = QUALITIES.map { |quality| triad(note, quality) }
      if accidental?(note) && simpler_enharmonic?(note: ENHARMONIC[note], other_note: note)
        chords + QUALITIES.map { |quality| triad(ENHARMONIC[note], quality) }
      else
        chords
      end
    end

    matching_chords = all_chords.select { |chord| notes.all? { |note| chord_includes_note?(chord, note) } }

    filtered_with_enharmonic_preference_for_requested_notes(
      chords: matching_chords,
      target_notes: notes
    )
  end
end

module AdjacentChords
  include Constants
  extend self

  def adjacent_chords(chord, semitone_freedom:)
    return [] if semitone_freedom.zero?

    [0, 1, 2].flat_map do |chord_tone_index|
      [
        chord.dup.tap { |c| c[chord_tone_index] = EngineV2.down(chord[chord_tone_index]) },
        chord.dup.tap { |c| c[chord_tone_index] = EngineV2.up(chord[chord_tone_index]) },
      ]
    end
  end

  private

  def note_up_semi(note)
    NOTE_MINOR2_UP.fetch(note)
  end

  def note_down_semi(note)
    NOTE_MINOR2_UP.invert.fetch(note)
  end
end
