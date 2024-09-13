def parsed_firewall(data)
  parsed = data.map do |line|
    line.strip.split(':')
        .map { |item| item.match(/\d+/)[0] }
        .map(&:to_i)
  end

  parsed.each_with_object({}) do |(depth, range), h|
    h[depth] = { range: range, sensor_pos: 0, direction: :down }
  end
end

def move_sensors!(firewall)
  firewall.each do |depth, sensor|
    if sensor[:direction] == :down
      if sensor[:sensor_pos] + 1 < sensor[:range]
        sensor_pos = sensor[:sensor_pos] + 1
        direction = :down
      else
        sensor_pos = sensor[:sensor_pos] - 1
        direction = :up
      end
    elsif sensor[:direction] == :up
      if sensor[:sensor_pos] - 1 >= 0
        sensor_pos = sensor[:sensor_pos] - 1
        direction = :up
      else
        sensor_pos = sensor[:sensor_pos] + 1
        direction = :down
      end
    end

    firewall[depth] = { range: sensor[:range], sensor_pos: sensor_pos, direction: direction }
  end
end

def part_one(data)
  firewall = parsed_firewall(data)
  low_depth, high_depth = firewall.keys.minmax

  severity = 0
  depth = low_depth - 1 # start one before the first real depth

  while depth <= high_depth
    depth += 1
    severity += (depth * firewall[depth][:range]) if firewall[depth] && firewall[depth][:sensor_pos].zero?
    move_sensors!(firewall)
  end

  severity
end

def visualize_depth(layer_depth, layer, pos, packet)
  brackets = pos.zero? && layer_depth == packet[:depth] ? '()' : '[]'
  unless layer
    return "#{brackets[0]}.#{brackets[1]}" if pos.zero? && layer_depth == packet[:depth]

    return '   '
  end
  brackets = '  ' if pos >= layer[:range]

  char = layer[:sensor_pos] == pos ? 'S' : ' '

  "#{brackets[0]}#{char}#{brackets[1]}"
end

def visualize(delayed_packets, firewall)
  return unless delayed_packets.size >= 11

  packet = delayed_packets[10]

  low_depth, high_depth = firewall.keys.minmax
  max_range = firewall.values.map { |sensor| sensor[:range] }.max

  labels = (low_depth..high_depth).map { |layer| " #{layer} " }.join
  puts labels
  pos = 0
  while pos < max_range
    puts (low_depth..high_depth).map { |layer| visualize_depth(layer, firewall[layer], pos, packet) }.join

    pos += 1
  end
  return unless packet[:time] >= 7

  p packet
  exit
end

def part_two(data)
  firewall = parsed_firewall(data)
  low_depth, high_depth = firewall.keys.minmax

  delayed_packets = [{ depth: low_depth - 1, caught: false, time: 0 }] # start one before the first real layer

  global_time = -1

  loop do
    target_packet = delayed_packets.find { |packet| packet[:depth] == high_depth && !packet[:caught] }
    return target_packet[:time] - target_packet[:depth] if target_packet

    global_time += 1
    delayed_packets.reject! { |packet| packet[:depth] > high_depth || packet[:caught] }
    delayed_packets.map! { |packet| { **packet, depth: packet[:depth] + 1, time: packet[:time] + 1 } }
    # visualize(delayed_packets, firewall)

    delayed_packets.each_with_index do |packet, delay|
      packet[:caught] = true if firewall[packet[:depth]] && firewall[packet[:depth]][:sensor_pos].zero?
    end

    move_sensors!(firewall)

    delayed_packets << { depth: low_depth - 1, caught: false, time: global_time }
  end
end

if __FILE__ == $0
  data = File.readlines('day_13_input.txt')
  p part_one(data)
  # Brute force is sufficient to solve this in about a minute.
  # It's not needed, but maybe there's a way to optimize by finding the cycles in the sensor movements?
  p part_two(data)
end
