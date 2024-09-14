class Node
  attr_reader :value
  attr_accessor :next_node

  def initialize(value, next_node = nil)
    @value = value
    @next_node = next_node
  end
end

class CircularLinkedList
  def initialize
    @head = nil
  end

  def insert_after(existing_node, value)
    new_node = Node.new(value)
    
    if @head.nil?
      # If the list is empty, initialize it with the new node
      @head = new_node
      new_node.next_node = @head
    else
      new_node.next_node = existing_node.next_node
      existing_node.next_node = new_node
    end
  
    new_node
  end

  def node_n_steps_forward(node, n_steps)
    current = node

    n_steps.times do
      current = current.next_node
    end
  
    current
  end

  def to_a
    array = []
    return array if @head.nil?

    current = @head

    loop do
      array << current.value
      current = current.next_node
      break if current == @head
    end

    array
  end
end

def part_one(n_steps)
  list = CircularLinkedList.new
  node = list.insert_after(nil, 0)

  (1..2017).each do |n|
    node = list.node_n_steps_forward(node, n_steps)
    node = list.insert_after(node, n)
  end

  node.next_node.value
end

if __FILE__ == $0
  p part_one(301) # sample
end
