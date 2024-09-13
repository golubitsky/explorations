require 'set'

def part_one(programs, dance_moves_raw)
  dance_moves_raw.split(',').each do |dance_move|
    case dance_move[0]
    when 's'
      n = dance_move[1..].to_i
      programs = programs[-n..] + programs[0...-n]
    when 'x'
      a, b = dance_move.scan(/\d+/).map(&:to_i)
      a_char = programs[a]
      b_char = programs[b]
      programs[a] = b_char
      programs[b] = a_char
    when 'p'
      a_char, b_char = dance_move[1..].split('/')
      a = programs.index(a_char)
      b = programs.index(b_char)
      programs[a] = b_char
      programs[b] = a_char
    end
  end

  programs
end

def part_two(programs, dance_moves_raw)
  n = 1
  64.times do
    programs = part_one(programs, dance_moves_raw)
    # manual cycle detection:
    puts n % 63 if programs == 'nlciboghjmfdapek' # cycle length is 63
    # 1000000000 % 63 => 55th item in the cycle will be the 1000000000th item in the sequence
    if n == 55
      p programs # answer!
    end
    n += 1
  end
end

if __FILE__ == $0
  data = File.read('day_16_input.txt')
  # p part_one('abcde', 's1,x3/4,pe/b') # sample
  # p part_one('abcdefghijklmnop', data)
  p part_two('abcdefghijklmnop', data)
end
