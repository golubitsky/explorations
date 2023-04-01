# frozen_string_literal: true

require 'json'

if __FILE__ == $PROGRAM_NAME
  file_name = ARGV.first
  file = File.read(file_name)
end
