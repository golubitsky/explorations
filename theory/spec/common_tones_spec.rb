require 'common_tones'

describe EngineV1 do
  describe '.note_interval_away' do
    subject(:note) { described_class.note_interval_away(**params) }

    [
      [{ note: 'C', interval: 'M2', direction: :up }, 'D'],
      [{ note: 'D', interval: 'M2', direction: :up }, 'E'],
      [{ note: 'D', interval: 'M2', direction: :down }, 'C'],
      [{ note: 'B', interval: 'M2', direction: :down }, 'A'],
    ].each do |(params, expected_note)|
      context "when #{params[:direction]} #{params[:interval]} from #{params[:note]}" do
        let(:params) { params }

        it { is_expected.to eq(expected_note) }
      end
    end
  end

  describe '.pivot_notes' do
    subject(:note) { described_class.pivot_notes(**params) }

    [
      [{ note: 'C', triad: :major, other_triad: :major, interval: 'M2', direction: :up }, []],
      [{ note: 'C', triad: :major, other_triad: :major, interval: 'P4', direction: :up }, ['C']],
      [{ note: 'Eb', triad: :major, other_triad: :major, interval: 'P4', direction: :down }, ['Bb']],
    ].each do |(params, expected_pivots)|
      context "when #{params[:direction]} #{params[:interval]} from #{params[:note]}" do
        let(:params) { params }

        it { is_expected.to eq(expected_pivots) }
      end
    end
  end
end
