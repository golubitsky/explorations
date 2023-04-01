class HuffmanTree
  attr_reader :root

  def initialize(frequency_table)
    raise ArgumentError, 'empty error table' unless frequency_table.count.positive?

    unused_nodes = leaf_nodes(frequency_table) # supposed to be a MinHeap

    until unused_nodes.length == 1
      unused_nodes.sort_by! { |node| [node.frequency, node.letter] }

      left = unused_nodes.shift
      right = unused_nodes.shift

      internal_node = HuffmanNode.new(
        frequency: left.frequency + right.frequency,
        left: left,
        right: right
      )

      unused_nodes << internal_node
    end

    @root = unused_nodes.first
  end

  private

  def leaf_nodes(frequencies)
    frequencies.map do |letter, frequency|
      HuffmanNode.new(
        frequency: frequency,
        letter: letter
      )
    end
  end
end

class HuffmanNode
  attr_reader :frequency, :letter, :left, :right

  # internal nodes do not have letters
  def initialize(frequency:, letter: nil, left: nil, right: nil)
    @frequency = frequency
    @letter = letter
    @left = left
    @right = right
  end
end
