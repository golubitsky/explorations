require 'set'

def parsed(data)
  parsed_lines = data.map { |line| line.split('<->').map { |a| a.scan(/\d+/).map(&:to_i) } }

  graph = Hash.new { |h, k| h[k] = [] }

  parsed_lines.each do |(node), edges|
    edges.each do |edge|
      graph[node] << edge
    end
  end

  graph
end

def part_one(data)
  graph = parsed(data)

  q = Queue.new
  seen = Set.new
  q.push(0)

  until q.empty?
    cur = q.pop
    unless seen.include?(cur)
      seen.add(cur)
      graph[cur].each { |node| q.push(node) }
    end
  end

  seen.size
end

if __FILE__ == $0
  data = File.readlines('day_12_input.txt')
  p part_one(data)
end
