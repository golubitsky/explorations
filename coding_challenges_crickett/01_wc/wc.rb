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

def call_wc(option:, string:)
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

def result_when_option_specified
  file_name = ARGV[1]

  string = if file_name.nil?
             $stdin.read
           else
             File.read(file_name)
           end

  result = call_wc(option: ARGV[0], string: string)

  formatted_line(results: [result], text: file_name)
end

def formatted_line(results:, text:)
  formatted_results = results
                      .map { |result| result.to_s.rjust(8, ' ') }
                      .join

  text_when_present = text.nil? ? '' : " #{text}"

  "#{formatted_results}#{text_when_present}"
end

def total(results)
  totals = Array.new(results.first[:results].count, 0)

  results.each do |result|
    result[:results].each_with_index do |item, index|
      totals[index] += item
    end
  end

  { results: totals, text: 'total' }
end

def result_when_only_file_names_specified
  file_names = ARGV

  results = file_names.map do |file_name|
    string = File.read(file_name)

    c = call_wc(option: '-c', string: string)
    l = call_wc(option: '-l', string: string)
    w = call_wc(option: '-w', string: string)

    { results: [l, w, c], text: file_name }
  end

  results.push(total(results)) if file_names.count > 1

  results.map { |result| formatted_line(**result) }
end

if __FILE__ == $PROGRAM_NAME
  case ARGV.first
  when /-/
    puts result_when_option_specified
  else
    puts result_when_only_file_names_specified
  end
end
