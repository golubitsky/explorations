def create_files(n)
  n_str = n.rjust(2, '0')

  ruby_file = "day_#{n_str}.rb"
  input_file = "day_#{n_str}_input.txt"
  sample_file = "day_#{n_str}_sample.txt"

  File.write(ruby_file, <<~RUBY)
    def part_one(data)
    end

    if __FILE__ == $0
      data = File.readlines("day_#{n_str}_sample.txt")
      part_one(data)
    end
  RUBY

  File.new(input_file, 'w').close
  File.new(sample_file, 'w').close

  puts "Files created: #{ruby_file}, #{input_file}, #{sample_file}"
end

create_files(ARGV[0]) if __FILE__ == $0
