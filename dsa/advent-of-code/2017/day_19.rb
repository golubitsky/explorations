require 'matrix'

VECTOR_BY_DIRECTION = {
  up: Vector[-1, 0],
  down: Vector[1, 0],
  left: Vector[0, -1],
  right: Vector[0, 1]
}.freeze

def start_pos(grid)
  Vector[0, grid.first.index('|')]
end

def new_direction_at_junction(pos, grid, direction)
  VECTOR_BY_DIRECTION.each do |new_direction, vector|
    next if vector + VECTOR_BY_DIRECTION[direction] == Vector[0, 0]

    new_pos = pos + vector
    return new_direction if grid[new_pos[0]] && grid[new_pos[0]][new_pos[1]] != ' '
  end
end

def next_pos(pos, direction)
  pos + VECTOR_BY_DIRECTION[direction]
end

def char(pos, grid)
  grid[pos[0]][pos[1]]
end

def part_one(data)
  grid = data.map { |x| x.gsub("\n", '') }
  letters = []
  pos = start_pos(grid)
  direction = :down
  loop do
    c = char(pos, grid)

    if ['|', '-'].include?(c)
      # keep going
    elsif c =~ /[A-Z]/
      letters << c
    elsif c == '+'
      direction = new_direction_at_junction(pos, grid, direction)
    else
      puts letters.join
      exit
    end
    pos = next_pos(pos, direction)
  end
end

if __FILE__ == $0
  data = File.readlines('day_19_input.txt')
  p part_one(data)
end
