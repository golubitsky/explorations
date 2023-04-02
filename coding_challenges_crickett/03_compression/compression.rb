# frozen_string_literal: true

require 'json'

require_relative 'lib/huffman_encoding'

if __FILE__ == $PROGRAM_NAME
  action, file_path = ARGV
  string = File.read(file_path)
  case action
  when '--encode'
    encoded = HuffmanEncoding.encoded(string).to_json
    File.write("#{file_path}-encoded", encoded)
    puts "encoded #{file_path} to #{file_path}-encoded"
  when '--decode'
  end
end
