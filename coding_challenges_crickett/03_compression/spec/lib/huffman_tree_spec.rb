# frozen_string_literal: true

RSpec.describe HuffmanTree do
  subject(:tree) { HuffmanTree.new(frequency_table) }

  context 'when no characters in frequency table' do
    let(:frequency_table) { {} }

    it 'raises ArgumentError' do
      expect { tree }.to raise_error(ArgumentError, 'empty error table')
    end
  end

  context 'when one character in frequency table' do
    let(:frequency_table) { { 'a' => 1 } }

    it 'returns HuffmanTree with just one node' do
      expect(tree.root.letter).to eq('a')
      expect(tree.root.frequency).to eq(1)
      expect(tree.root.left_child).to eq(nil)
      expect(tree.root.right_child).to eq(nil)
    end
  end

  context 'when two characters in frequency table' do
    let(:frequency_table) { { 'a' => 1, 'b' => 2 } }

    specify 'root is internal node with total of all frequencies' do
      expect(tree.root.letter).to eq(nil)
      expect(tree.root.frequency).to eq(3)
    end

    specify 'left child is least frequent of the two letters' do
      expect(tree.root.left_child.letter).to eq('a')
      expect(tree.root.left_child.frequency).to eq(1)
    end

    specify 'left child is most frequent of the two letters' do
      expect(tree.root.right_child.letter).to eq('b')
      expect(tree.root.right_child.frequency).to eq(2)
    end
  end
end
