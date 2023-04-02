# frozen_string_literal: true

require 'json'

require_relative 'lib/huffman_encoding'

def encode(string, input_file_path)
  File.write(
    "#{input_file_path}-encoded",
    HuffmanEncoding.encoded(string)
  )

  puts "encoded #{input_file_path} to #{input_file_path}-encoded"
end

def decode(string, input_file_path)
  File.write(
    "#{input_file_path}-decoded",
    HuffmanEncoding.decoded(string)
  )

  puts "decoded #{input_file_path} to #{input_file_path}-decoded"
end

if __FILE__ == $PROGRAM_NAME
  action, input_file_path = ARGV
  string = File.read(input_file_path)

  case action
  when '--encode'
    encode(string, input_file_path)
  when '--decode'
    decode(string, input_file_path)
  end
end
