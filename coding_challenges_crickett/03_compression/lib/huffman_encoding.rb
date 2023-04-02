# frozen_string_literal: false

require 'json'

require_relative 'huffman_tree'
require_relative 'char_frequency'

EIGHT_BIT_UNSIGNED_PACK_DIRECTIVE = 'C*'

module HuffmanEncoding
  extend self

  def encoded(string)
    tree = HuffmanTree.new(
      CharFrequency.char_frequency_table(string)
    )

    if tree.prefix_code_table.size > 128
      raise 'encoding more than 128 unique characters is not supported'
    end

    table = tree.prefix_code_table

    {
      utf_8_json_decoding_table_hash_as_string: table.invert.to_s,
      binary_string: encoded_binary_string(string, table)
    }
  end

  def decoded(utf_8_json_decoding_table_hash_as_string:, binary_string:)
    # TODO: remove security risk by storing the table in a better way
    decoding_table = eval(utf_8_json_decoding_table_hash_as_string)

    i = 0
    j = 0

    decoded = ''

    while i < binary_string.length
      window = binary_string[i..j]

      if decoding_table[window]
        decoded << decoding_table[window]
        i = j + 1
        j = i
      else
        j += 1
      end
    end

    decoded
  end

  private

  def encoded_binary_string(string, encoding_table)
    string.chars
          .map { |char| encoding_table[char] }
          .join
  end
end
