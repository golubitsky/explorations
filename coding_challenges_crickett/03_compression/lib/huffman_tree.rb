class HuffmanTree
  attr_reader :root

  def initialize(frequency_table)
    raise ArgumentError, 'empty error table' unless frequency_table.count.positive?

    unused_nodes = leaf_nodes(frequency_table) # supposed to be a MinHeap

    until unused_nodes.length == 1
      unused_nodes.sort_by!(&:frequency)

      left_child = unused_nodes.shift
      right_child = unused_nodes.shift

      internal_node = HuffmanNode.new(
        frequency: left_child.frequency + right_child.frequency,
        left_child: left_child,
        right_child: right_child
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
  attr_reader :frequency, :letter, :left_child, :right_child

  # internal nodes do not have letters
  def initialize(frequency:, letter: nil, left_child: nil, right_child: nil)
    @frequency = frequency
    @letter = letter
    @left_child = left_child
    @right_child = right_child
  end
end
