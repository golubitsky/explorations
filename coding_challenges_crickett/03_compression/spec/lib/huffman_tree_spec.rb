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
      expect(tree.root.left).to eq(nil)
      expect(tree.root.right).to eq(nil)
    end
  end

  context 'when two characters in frequency table' do
    let(:frequency_table) { { 'a' => 1, 'b' => 2 } }

    specify 'root is internal node with total of all frequencies' do
      expect(tree.root.letter).to eq(nil)
      expect(tree.root.frequency).to eq(3)
    end

    specify 'left child is least frequent of the two letters' do
      expect(tree.root.left.letter).to eq('a')
      expect(tree.root.left.frequency).to eq(1)
    end

    specify 'left child is most frequent of the two letters' do
      expect(tree.root.right.letter).to eq('b')
      expect(tree.root.right.frequency).to eq(2)
    end
  end

  context 'when example from https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/Huffman.html' do
    let(:frequency_table) do
      {
        'C' => 32,
        'D' => 42,
        'E' => 120,
        'K' => 7,
        'L' => 42,
        'M' => 24,
        'U' => 37,
        'Z' => 2
      }
    end

    it 'puts E in correct place' do
      node = tree.root.left
      expect(node.letter).to eq('E')
      expect(node.frequency).to eq(120)
    end

    it 'puts U in correct place' do
      node = tree.root.right.left.left
      expect(node.letter).to eq('U')
      expect(node.frequency).to eq(37)
    end

    it 'puts D in correct place' do
      node = tree.root.right.left.right
      expect(node.letter).to eq('D')
      expect(node.frequency).to eq(42)
    end

    it 'puts L in correct place' do
      node = tree.root.right.right.left
      expect(node.letter).to eq('L')
      expect(node.frequency).to eq(42)
    end

    it 'puts C in correct place' do
      node = tree.root.right.right.right.left
      expect(node.letter).to eq('C')
      expect(node.frequency).to eq(32)
    end

    it 'puts M in correct place' do
      node = tree.root.right.right.right.right.right
      expect(node.letter).to eq('M')
      expect(node.frequency).to eq(24)
    end

    it 'puts Z in correct place' do
      node = tree.root.right.right.right.right.left.left
      expect(node.letter).to eq('Z')
      expect(node.frequency).to eq(2)
    end

    it 'puts K in correct place' do
      node = tree.root.right.right.right.right.left.right
      expect(node.letter).to eq('K')
      expect(node.frequency).to eq(7)
    end
  end
end
