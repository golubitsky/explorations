require 'matrix'

def parsed_ints(string)
  string.scan(/-?\d+/).map(&:to_i)
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

def solution(data, part = 1)
  particles = parsed_particles(data)

  last_index = -1
  count = 0

  loop do
    collision_hash = Hash.new { |h, k| h[k] = [] }

    particles = particles.map.with_index do |particle, index|
      updated = updated_particle(particle)
      collision_hash[updated[:position]] << index

      updated
    end

    if part == 2
      indexes_to_remove = []
      collision_hash.each_value do |indexes|
        indexes_to_remove += indexes if indexes.count > 1
      end

      particles.reject!.with_index { |_, index| indexes_to_remove.include?(index) }
    end

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
    if count == arbitrary_threshold
      return last_index if part == 1
      return particles.count if part == 2
    end
  end
end

if __FILE__ == $0
  data = File.readlines('day_20_input.txt')
  pp solution(data, part = 2)
end
