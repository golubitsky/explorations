require 'spec_helper'
require 'engine_v2'

describe EngineV2 do
  describe '.up' do
    [
      ['C', 'C#'],
      ['D', 'D#'],
      ['F', 'F#'],
      ['G', 'G#'],
      ['A', 'A#'],
    ].each do |(input, expected)|
      it "returns simple sharp #{expected} from #{input}" do
        expect(EngineV2.up(input)).to eq(expected)
      end
    end

    [
      %w[B C],
      %w[E F],
    ].each do |(input, expected)|
      it "returns white key adjacent up #{expected} from #{input}" do
        expect(EngineV2.up(input)).to eq(expected)
      end
    end

    [
      %w[Bb B],
      %w[Eb E],
      %w[Ab A],
      %w[Db D],
      %w[Gb G],
    ].each do |(input, expected)|
      it "returns unflatted #{expected} from #{input}" do
        expect(EngineV2.up(input)).to eq(expected)
      end
    end

    [
      ['C#', 'D'],
      ['D#', 'E'],
      ['F#', 'G'],
      ['G#', 'A'],
      ['A#', 'B'],
      ['B#', 'C#'],
      ['E#', 'F#'],
    ].each do |(input, expected)|
      it "returns next note #{expected} from #{input}" do
        expect(EngineV2.up(input)).to eq(expected)
      end
    end
  end

  describe '.down' do
    [
      %w[B Bb],
      %w[E Eb],
      %w[A Ab],
      %w[D Db],
      %w[G Gb],
    ].each do |(input, expected)|
      it "returns simple sharp #{expected} from #{input}" do
        expect(EngineV2.down(input)).to eq(expected)
      end
    end

    # roll up
    [
      %w[C B],
      %w[F E],
    ].each do |(input, expected)|
      it "returns white key adjacent down #{expected} from #{input}" do
        expect(EngineV2.down(input)).to eq(expected)
      end
    end

    # sharps
    [
      %w[G# G],
      %w[C# C],
      %w[F# F],
      %w[D# D],
      %w[A# A],
    ].each do |(input, expected)|
      it "returns unflatted #{expected} from #{input}" do
        expect(EngineV2.down(input)).to eq(expected)
      end
    end

    [
      %w[Bb A],
      %w[Eb D],
      %w[Ab G],
      %w[Db C],
      %w[Gb F],
      %w[Cb Bb],
      %w[Fb Eb],
    ].each do |(input, expected)|
      it "returns next note #{expected} from #{input}" do
        expect(EngineV2.down(input)).to eq(expected)
      end
    end
  end
end
