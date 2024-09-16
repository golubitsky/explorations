require 'matrix'

def parsed_ints(string)
  string.scan(/\d+/).map(&:to_i)
end

def parsed_particles(data)
  data.map do |line|
    position, velocity, acceleration = line.split(', ')
    {
      position: Vector[*parsed_ints(position)],
      velocity: Vector[*parsed_ints(velocity)],
      acceleration: Vector[*parsed_ints(acceleration)]
    }
  end
end

def updated_particle(particle)
  particle[:velocity] += particle[:acceleration]
  particle[:position] += particle[:velocity]
  particle
end

def manhattan_distance(particle)
  pos = particle[:position]
  pos[0].abs + pos[1].abs + pos[2].abs
end

def index_of_min_distance(particles)
  lowest = Float::INFINITY
  lowest_index = -1

  particles.each_with_index do |particle, index|
    m = manhattan_distance(particle)
    if m < lowest
      lowest = m
      lowest_index = index
    end
  end

  lowest_index
end

def part_one(data)
  particles = parsed_particles(data)

  last_index = -1
  count = 0

  loop do
    particles.map! { |particle| updated_particle(particle) }

    cur_low_index = index_of_min_distance(particles)

    if cur_low_index == last_index
      count += 1
    else
      count = 1
    end

    last_index = cur_low_index

    # heuristic: assume that if the same particle is closest n times in a row
    # it will always be closest
    arbitrary_threshold = 100
    return last_index if count == arbitrary_threshold
  end
end

if __FILE__ == $0
  data = File.readlines('day_20_input.txt')
  pp part_one(data)
end
