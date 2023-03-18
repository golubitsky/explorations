# frozen_string_literal: true

def byte_count(string)
  string.bytesize
end

def line_count(string)
  string.split("\n").count
end

def word_count(string)
  string.split.count
end

def char_count(string)
  string.length
end

def result(option:, string:)
  case option
  when '-c'
    byte_count(string)
  when '-l'
    line_count(string)
  when '-w'
    word_count(string)
  when '-m'
    char_count(string)
  end
end

def formatted(result)
  result.to_s.rjust(8, ' ')
end

def result_when_option_specified
  file_name = ARGV[1]
  string = if file_name.nil?
             $stdin.read
           else
             File.read(file_name)
           end

  result = formatted(result(option: ARGV[0], string: string))
  file_name_when_present = file_name.nil? ? '' : " #{file_name}"

  "#{result}#{file_name_when_present}"
end

def result_when_only_file_name_specified
  file_name = ARGV[0]
  string = File.read(file_name)

  c = formatted(result(option: '-c', string: string))
  l = formatted(result(option: '-l', string: string))
  w = formatted(result(option: '-w', string: string))

  "#{l}#{w}#{c} #{file_name}"
end

if __FILE__ == $PROGRAM_NAME
  case ARGV.first
  when /-/
    puts result_when_option_specified
  else
    puts result_when_only_file_name_specified
  end
end
