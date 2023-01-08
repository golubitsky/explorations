require 'common_tones'

describe EngineV1 do
  describe '.note_interval_away' do
    subject(:note) { described_class.note_interval_away(**p) }

    [
      [{ note: 'C', interval: 'M2', direction: :up }, 'D'],
      [{ note: 'D', interval: 'M2', direction: :up }, 'E'],
      [{ note: 'D', interval: 'M2', direction: :down }, 'C'],
      [{ note: 'B', interval: 'M2', direction: :down }, 'A'],
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
      [{ note: 'C', triad: :major, other_triad: :major, interval: 'M2', direction: :up }, []],
      [{ note: 'C', triad: :major, other_triad: :major, interval: 'P4', direction: :up }, ['C']],
      [{ note: 'Eb', triad: :major, other_triad: :major, interval: 'P4', direction: :down }, ['Bb']],
      [{ note: 'C', triad: :major, other_triad: :major, interval: 'P4', direction: :up }, ['C']],
      [{ note: 'C', triad: :major, other_triad: :major, interval: 'P5', direction: :up }, ['G']],
      [{ note: 'E', triad: :major, other_triad: :major, interval: 'P5', direction: :down }, ['E']],
      # minor
      [{ note: 'F', triad: :minor, other_triad: :minor, interval: 'm3', direction: :up }, ['Ab']],
      # minor to major
      [{ note: 'C', triad: :minor, other_triad: :major, interval: 'm3', direction: :up }, %w[Eb G]],
      # minor to dim
      [{ note: 'C', triad: :minor, other_triad: :diminished, interval: 'm3', direction: :down }, %w[C Eb]],
      # major to dim
      [{ note: 'C', triad: :major, other_triad: :diminished, interval: 'M3', direction: :up }, %w[E G]],
    ].each do |(p, expected_pivots)|
      context "when #{p[:other_triad]} #{p[:direction]} #{p[:interval]} from #{p[:note]} #{p[:triad]}" do
        let(:p) { p }

        it { is_expected.to eq(expected_pivots) }
      end
    end
  end
end
