# frozen_string_literal: true

require 'json'

require_relative 'lib/huffman_encoding'

BIT_STRING_MSB_FIRST_DIRECTIVE = 'B*'

def encode(input_file_path)
  string = File.read(input_file_path)

  encoded_path = "#{input_file_path}-encoded"
  table_path = "#{input_file_path}-table"

  encoded_result = HuffmanEncoding.encoded(string)

  File.binwrite(encoded_path,
                [encoded_result[:binary_string]].pack(BIT_STRING_MSB_FIRST_DIRECTIVE))
  File.write(table_path,
             encoded_result[:utf_8_json_decoding_table_hash_as_string])

  puts "encoded #{input_file_path} to #{encoded_path}"
  puts "stored decoding table at #{table_path}"
end

def decode(input_file_path, decoding_table_file_path)
  string = File.binread(input_file_path).unpack1(BIT_STRING_MSB_FIRST_DIRECTIVE)
  decoding_table = File.read(decoding_table_file_path)

  decoded_path = "#{input_file_path}-decoded"

  decoded_result = HuffmanEncoding.decoded(
    binary_string: string,
    utf_8_json_decoding_table_hash_as_string: decoding_table
  )

  File.write(decoded_path, decoded_result)

  puts "decoded #{input_file_path} to #{decoded_path}"
end

if __FILE__ == $PROGRAM_NAME

  case ARGV[0]
  when '--encode'
    input_file_path = ARGV[1]
    encode(input_file_path)
  when '--decode'
    input_file_path, decoding_table_file_path = ARGV[1..2]

    decode(input_file_path, decoding_table_file_path)
  end
end
