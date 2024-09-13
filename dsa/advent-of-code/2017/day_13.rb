def parsed_firewall(data)
  parsed = data.map do |line|
    line.strip.split(':')
        .map { |item| item.match(/\d+/)[0] }
        .map(&:to_i)
  end

  parsed.each_with_object({}) do |(depth, range), h|
    h[depth] = { range: range, pos: 0, direction: :down }
  end
end

def move_sensors!(firewall)
  firewall.each do |depth, sensor|
    # p "#{depth}, #{sensor[:range]}, #{sensor[:pos].inspect}"

    if sensor[:direction] == :down
      if sensor[:pos] + 1 < sensor[:range]
        pos = sensor[:pos] + 1
        direction = :down
      else
        pos = sensor[:pos] - 1
        direction = :up
      end
    elsif sensor[:direction] == :up
      if sensor[:pos] - 1 >= 0
        pos = sensor[:pos] - 1
        direction = :up
      else
        pos = sensor[:pos] + 1
        direction = :down
      end
    end

    firewall[depth] = { range: sensor[:range], pos: pos, direction: direction }
  end
end

def part_one(data)
  firewall = parsed_firewall(data)
  low_layer, high_layer = firewall.keys.minmax

  severity = 0
  layer = low_layer - 1 # start one before the first real layer

  while layer <= high_layer
    layer += 1
    severity += (layer * firewall[layer][:range]) if firewall[layer] && firewall[layer][:pos].zero?
    move_sensors!(firewall)
  end

  severity
end

if __FILE__ == $0
  data = File.readlines('day_13_input.txt')
  p part_one(data)
end
