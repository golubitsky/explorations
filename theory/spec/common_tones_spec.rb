# frozen_string_literal: true

require 'spec_helper'
require 'common_tones'

describe EngineV1 do
  describe '.note_interval_away' do
    subject(:note) { described_class.note_interval_away(**p) }

    [
      [{ note: 'C', interval: :M2, direction: :up }, 'D'],
      [{ note: 'D', interval: :M2, direction: :up }, 'E'],
      [{ note: 'D', interval: :M2, direction: :down }, 'C'],
      [{ note: 'B', interval: :M2, direction: :down }, 'A'],
      [{ note: 'Eb', interval: :m3, direction: :up }, 'Gb'],
    ].each do |(p, expected_note)|
      context "when #{p[:direction]} #{p[:interval]} from #{p[:note]}" do
        let(:p) { p }

        it { is_expected.to eq(expected_note) }
      end
    end
  end

  describe '.pivot_notes' do
    subject(:note) { described_class.pivot_notes(**p) }

    [
      # major
      [{ note: 'C', quality: :major, other_quality: :major, interval: :M2, direction: :up }, []],
      [{ note: 'C', quality: :major, other_quality: :major, interval: :P4, direction: :up }, ['C']],
      [{ note: 'Eb', quality: :major, other_quality: :major, interval: :P4, direction: :down }, ['Bb']],
      [{ note: 'C', quality: :major, other_quality: :major, interval: :P4, direction: :up }, ['C']],
      [{ note: 'C', quality: :major, other_quality: :major, interval: :P5, direction: :up }, ['G']],
      [{ note: 'E', quality: :major, other_quality: :major, interval: :P5, direction: :down }, ['E']],
      # minor
      [{ note: 'F', quality: :minor, other_quality: :minor, interval: :m3, direction: :up }, ['Ab']],
      # minor to major
      [{ note: 'C', quality: :minor, other_quality: :major, interval: :m3, direction: :up }, %w[Eb G]],
      # minor to dim
      [{ note: 'C', quality: :minor, other_quality: :diminished, interval: :m3, direction: :down }, %w[C Eb]],
      # major to dim
      [{ note: 'C', quality: :major, other_quality: :diminished, interval: :M3, direction: :up }, %w[E G]],
      [{ note: 'C', quality: :major, other_quality: :diminished, interval: :m2, direction: :up }, %w[E G]],
    ].each do |(p, expected_pivots)|
      context "when #{p[:other_quality]} #{p[:direction]} #{p[:interval]} from #{p[:note]} #{p[:quality]}" do
        let(:p) { p }

        it { is_expected.to eq(expected_pivots) }
      end
    end
  end
end
