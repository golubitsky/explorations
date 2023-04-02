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

  describe 'example from https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/Huffman.html' do
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

    it 'processes char E' do
      node = tree.root.left
      expect(node.letter).to eq('E')
      expect(node.frequency).to eq(120)
      expect(tree.prefix_code_table['E']).to eq('0')
    end

    it 'processes char U' do
      node = tree.root.right.left.left
      expect(node.letter).to eq('U')
      expect(node.frequency).to eq(37)
      expect(tree.prefix_code_table['U']).to eq('100')
    end

    it 'processes char D' do
      node = tree.root.right.left.right
      expect(node.letter).to eq('D')
      expect(node.frequency).to eq(42)
      expect(tree.prefix_code_table['D']).to eq('101')
    end

    it 'processes char L' do
      node = tree.root.right.right.left
      expect(node.letter).to eq('L')
      expect(node.frequency).to eq(42)
      expect(tree.prefix_code_table['L']).to eq('110')
    end

    it 'processes char C' do
      node = tree.root.right.right.right.left
      expect(node.letter).to eq('C')
      expect(node.frequency).to eq(32)
      expect(tree.prefix_code_table['C']).to eq('1110')
    end

    it 'processes char M' do
      node = tree.root.right.right.right.right.right
      expect(node.letter).to eq('M')
      expect(node.frequency).to eq(24)
      expect(tree.prefix_code_table['M']).to eq('11111')
    end

    it 'processes char Z' do
      node = tree.root.right.right.right.right.left.left
      expect(node.letter).to eq('Z')
      expect(node.frequency).to eq(2)
      expect(tree.prefix_code_table['Z']).to eq('111100')
    end

    it 'processes char K' do
      node = tree.root.right.right.right.right.left.right
      expect(node.letter).to eq('K')
      expect(node.frequency).to eq(7)
      expect(tree.prefix_code_table['K']).to eq('111101')
    end
  end

  describe 'example from Huffman Coding | GeeksforGeeks' do
    # see https://www.youtube.com/watch?v=0kNXhFIEd_w

    let(:frequency_table) do
      {
        'a' => 5,
        'b' => 9,
        'c' => 12,
        'd' => 13,
        'e' => 16,
        'f' => 45
      }
    end

    it 'processes char a' do
      node = tree.root.right.right.left.left
      expect(node.letter).to eq('a')
      expect(node.frequency).to eq(5)
      expect(tree.prefix_code_table['a']).to eq('1100')
    end

    it 'processes char b' do
      node = tree.root.right.right.left.right
      expect(node.letter).to eq('b')
      expect(node.frequency).to eq(9)
      expect(tree.prefix_code_table['b']).to eq('1101')
    end

    it 'processes char c' do
      node = tree.root.right.left.left
      expect(node.letter).to eq('c')
      expect(node.frequency).to eq(12)
      expect(tree.prefix_code_table['c']).to eq('100')
    end

    it 'processes char d' do
      node = tree.root.right.left.right
      expect(node.letter).to eq('d')
      expect(node.frequency).to eq(13)
      expect(tree.prefix_code_table['d']).to eq('101')
    end

    it 'processes char e' do
      node = tree.root.right.right.right
      expect(node.letter).to eq('e')
      expect(node.frequency).to eq(16)
      expect(tree.prefix_code_table['e']).to eq('111')
    end

    it 'processes char f' do
      node = tree.root.left
      expect(node.letter).to eq('f')
      expect(node.frequency).to eq(45)
      expect(tree.prefix_code_table['f']).to eq('0')
    end
  end

  describe 'integration test using Les Miserables text input' do
    let(:string) { File.read('spec/data/135-0.txt') }
    let(:frequency_table) { CharFrequency.char_frequency_table(string) }

    it 'produces the tree' do
      expect(tree).not_to be_nil
    end
  end
end
