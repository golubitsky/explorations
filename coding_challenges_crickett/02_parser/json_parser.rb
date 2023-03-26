# frozen_string_literal: true

require 'json'

if __FILE__ == $PROGRAM_NAME
  file_name = ARGV.first
  file = File.read(file_name)

  begin
    JSON.parse(file)
    puts "#{file_name} is valid JSON"
    exit(0)
  rescue JSON::ParserError
    puts "#{file_name} is invalid JSON"
    exit(1)
  end
end
