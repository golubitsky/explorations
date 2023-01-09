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
      # major to augmented
      [{ note: 'Bb', quality: :major, other_quality: :augmented, interval: :P1, direction: :up }, %w[Bb D]],
      # dim to dim
      [{ note: 'Bb', quality: :diminished, other_quality: :diminished, interval: :M6, direction: :up }, %w[Bb Db]],
    ].each do |(p, expected_pivots)|
      context "when #{p[:other_quality]} #{p[:direction]} #{p[:interval]} from #{p[:note]} #{p[:quality]}" do
        let(:p) { p }

        it { is_expected.to eq(expected_pivots) }
      end
    end
  end

  describe '.pivot_chords' do
    subject(:chord) { described_class.pivot_chords(notes) }

    context 'when one note (Eb)' do
      let(:notes) { %w[Eb] }

      it 'contains dim chord where note is 5th' do
        expect(chord).to include(%w[A C Eb])
      end

      it 'contains min chord where note is 5th' do
        expect(chord).to include(%w[Ab Cb Eb])
      end

      it 'contains maj chord where note is 5th' do
        expect(chord).to include(%w[Ab C Eb])
      end

      xit 'contains aug chord where note is 5th' do
        # not sure how to get this to pass.. use enharmonic equivalent?
        expect(chord).to include(%w[Abb Cb Eb])
      end

      it 'contains dim chord where note is 3rd' do
        expect(chord).to include(%w[C Eb Gb])
      end

      it 'contains min chord where note is 3rd' do
        expect(chord).to include(%w[C Eb G])
      end

      xit 'contains maj chord where note is 3rd' do
        expect(chord).to include(%w[Cb Eb Gb])
      end

      xit 'contains aug chord where note is 3rd' do
        expect(chord).to include(%w[Cb Eb G])
      end

      it 'contains dim chord where note is root' do
        expect(chord).to include(%w[Eb Gb Bbb])
      end

      it 'contains min chord where note is root' do
        expect(chord).to include(%w[Eb Gb Bb])
      end

      it 'contains maj chord where note is root' do
        expect(chord).to include(%w[Eb G Bb])
      end

      it 'contains aug chord where note is root' do
        expect(chord).to include(%w[Eb G B])
      end
    end

    context 'when two notes' do
      let(:notes) { %w[A C] }

      it 'returns all chords that contain both notes' do
        expect(chord).to contain_exactly(
          %w[A C E],
          %w[F A C],
          %w[A C Eb],
          %w[F# A C]
        )
      end
    end

    context 'when two notes that do not form a chord (according to the engine)' do
      let(:notes) { %w[A B] }

      it 'returns no chords' do
        expect(chord).to eq([])
      end
    end
  end
end
