module HuffmanEncoding
  extend self

  def encoded(string)
    tree = HuffmanTree.new(
      CharFrequency.char_frequency_table(string)
    )

    {
      decoding_table: tree.prefix_code_table.invert,
      encoded_string: encoding(string, tree.prefix_code_table)
    }
  end

  def decoded(encoded)
    left_index = 0
    right_index = 0

    decoded_string = ''

    while left_index < encoded[:encoded_string].length
      window = encoded[:encoded_string][left_index..right_index]

      decoded_char = encoded[:decoding_table][window]

      if decoded_char
        decoded_string << decoded_char
        left_index, right_index = right_index + 1, left_index
      else
        right_index += 1
      end
    end

    decoded_string
  end

  private

  def encoding(string, table)
    string.chars.map { |char| table[char] }.join
  end
end
