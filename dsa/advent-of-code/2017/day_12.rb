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

def bfs(node, graph, seen = Set.new)
  q = Queue.new
  q.push(node)

  until q.empty?
    cur = q.pop
    unless seen.include?(cur)
      seen.add(cur)
      graph[cur].each { |node| q.push(node) }
    end
  end

  seen
end

def part_one(data)
  graph = parsed(data)

  bfs(0, graph).size
end

def part_two(data)
  graph = parsed(data)

  seen = Set.new
  group_count = 0

  graph.each_key do |node|
    next if seen.include?(node)

    seen = bfs(node, graph, seen)
    group_count += 1
  end

  group_count
end

if __FILE__ == $0
  data = File.readlines('day_12_input.txt')
  p part_one(data)
  p part_two(data)
end
