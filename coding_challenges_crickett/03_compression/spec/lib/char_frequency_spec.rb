# frozen_string_literal: true

RSpec.describe CharFrequency do
  subject(:table) { CharFrequency.char_frequency_table(string) }

  context 'when one character' do
    let(:string) { 'a' }

    it 'returns frequency table' do
      expect(table).to eq({ 'a' => 1 })
    end
  end

  context 'when repeated character' do
    let(:string) { 'aa' }

    it 'counts them as repeated' do
      expect(table).to eq({ 'a' => 2 })
    end
  end

  context 'when two different chars' do
    let(:string) { 'ab' }

    it 'returns frequency table' do
      expect(table).to eq({ 'a' => 1, 'b' => 1 })
    end
  end

  context 'when same letter but uppercase and lowercase' do
    let(:string) { 'aA' }

    it 'differentiates them as different chars' do
      expect(table).to eq({ 'a' => 1, 'A' => 1 })
    end
  end

  context 'when spaces' do
    let(:string) { 'a c' }

    it 'differentiates them as a char' do
      expect(table).to eq({ 'a' => 1, 'c' => 1, ' ' => 1 })
    end
  end

  context 'when Les Miserables test input' do
    let(:string) { File.read('spec/data/135-0.txt') }

    it "finds 333 occurrences of 'X'" do
      expect(table['X']).to eq(333)
    end

    it "finds 223000 occurrences of 't'" do
      expect(table['t']).to eq(223_000)
    end
  end
end
