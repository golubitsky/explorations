# frozen_string_literal: true

class HuffmanTree
  attr_reader :root, :prefix_code_table

  def initialize(frequency_table)
    raise ArgumentError, 'empty error table' unless frequency_table.count.positive?

    @root = root_node_of_generated_huffman_tree(frequency_table)
    @prefix_code_table = generate_prefix_code_table
  end

  private

  def root_node_of_generated_huffman_tree(frequency_table)
    unused_nodes = leaf_nodes(frequency_table)

    until unused_nodes.length == 1
      left_child, right_child = extract_two_least_frequent_letters(unused_nodes)
      unused_nodes << new_internal_node(left_child, right_child)
    end

    unused_nodes.first
  end

  def new_internal_node(left_child, right_child)
    HuffmanNode.new(
      frequency: left_child.frequency + right_child.frequency,
      left: left_child,
      right: right_child
    )
  end

  def extract_two_least_frequent_letters(nodes)
    nodes.sort_by! do |node|
      [
        node.frequency,
        # node.letter: break ties when two chars occur with same frequency
        # to_s: without it seeing error "comparison of Array with Array failed"
        node.letter.to_s
      ]
    end

    nodes.shift(2)
  end

  def leaf_nodes(frequencies)
    frequencies.map do |letter, frequency|
      HuffmanNode.new(
        frequency: frequency,
        letter: letter
      )
    end
  end

  def generate_prefix_code_table
    table = {}

    traverse_tree_with_code_so_far(table, node: root, code_so_far: '') do |node, code_so_far|
      # internal nodes don't have letters; don't assign them values in prefix code table
      table[node.letter] = code_so_far if node.letter
    end

    table
  end

  def traverse_tree_with_code_so_far(table, node:, code_so_far:, &block)
    return unless node

    left_code = "#{code_so_far}0"
    right_code = "#{code_so_far}1"
    traverse_tree_with_code_so_far(table, node: node.left, code_so_far: left_code, &block)
    yield(node, code_so_far)
    traverse_tree_with_code_so_far(table, node: node.right, code_so_far: right_code, &block)
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
