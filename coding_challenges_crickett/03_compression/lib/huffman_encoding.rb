# frozen_string_literal: true

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
    # HACK: strip leading zeros and simplify representation of most common char
    # this should be moved to the generation of the prefix_code_table
    table = tree.prefix_code_table.transform_values do |bit_string|
      bit_string.chars.uniq == ['0'] ? '0' : bit_string.sub(/^0*/, '')
    end

    {
      utf_8_json_decoding_table_hash_as_string: table.invert.to_s,
      encoded_string: encoded_string(string, table)
    }
  end

  def decoded(utf_8_json_decoding_table_hash_as_string:, encoded_string:)
    # TODO: remove security risk by storing the table in a better way
    decoding_table = eval(utf_8_json_decoding_table_hash_as_string)
    unpacked = encoded_string.unpack(EIGHT_BIT_UNSIGNED_PACK_DIRECTIVE)
    bit_strings = unpacked.map { |i| i.to_s(2) }

    bit_strings.map { |bit_string| decoding_table[bit_string] }
               .join
  end

  private

  def binary_representation(bit_string:)
    bit_string.to_i(2)
  end

  def bit_strings_to_be_packed(string, table)
    string.chars.map { |char| table[char] }
  end

  def encoded_string(string, table)
    if table.size > 128
      raise 'encoding more than 128 unique characters is not supported'
    end

    bit_strings_to_be_packed(string, table)
      .map { |bit_string| binary_representation(bit_string: bit_string) }
      .pack(EIGHT_BIT_UNSIGNED_PACK_DIRECTIVE)
  end
end
