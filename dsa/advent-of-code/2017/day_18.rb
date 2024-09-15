SEND = 'snd'
SET = 'set'
ADD = 'add'
MULTIPLY = 'mul'
REMAINDER = 'mod'
RECEIVE = 'rcv'
JUMP = 'jgz'

def integer?(str)
  Integer(str)
  true
rescue ArgumentError
  false
end

def parsed_value(raw_value, registers)
  return nil if raw_value.nil?

  if integer?(raw_value)
    raw_value.to_i
  else
    registers[raw_value]
  end
end

def part_one(data)
  registers = Hash.new(0)
  i = 0
  sound = nil

  while i < data.length
    instruction, register, raw_value = data[i].split
    value = parsed_value(raw_value, registers)

    case instruction
    when SEND
      sound = registers[register]
    when SET
      registers[register] = value
    when ADD
      registers[register] += value
    when MULTIPLY
      registers[register] *= value
    when REMAINDER
      registers[register] %= value
    when RECEIVE
      return sound unless registers[register].zero?
    when JUMP
      check = integer?(register) ? register.to_i : registers[register]
      if check.positive?
        i += value
        next
      end
    end
    i += 1
  end
end

class Program
  attr_reader :data, :registers, :q, :send_count

  def initialize(data, id)
    @index = 0
    @data = data
    @registers = Hash.new(0)
    registers['p'] = id
    @q = Queue.new
    @send_count = 0
  end

  def check_if_done
    :done if @index == data.length
  end

  def process_next_instruction
    return check_if_done if check_if_done

    # puts "program #{registers['p']}: #{@index + 1}"
    instruction, register, raw_value = data[@index].split
    value = parsed_value(raw_value, registers)

    case instruction
    when SEND
      send_value = integer?(register) ? register.to_i : registers[register]
      @index += 1
      @send_count += 1
      return send_value
    when SET
      registers[register] = value
    when ADD
      registers[register] += value
    when MULTIPLY
      registers[register] *= value
    when REMAINDER
      registers[register] %= value
    when RECEIVE
      return :waiting if q.empty?

      registers[register] = q.pop
    when JUMP
      check = integer?(register) ? register.to_i : registers[register]
      if check.positive?
        @index += value
        return
      end
    end
    @index += 1

    check_if_done
  end

  def enqueue(value)
    @q << value
  end
end

def part_two(data) # AKA operating system?
  zero = Program.new(data, 0)
  one = Program.new(data, 1)

  loop do
    result_zero = zero.process_next_instruction
    result_one = one.process_next_instruction

    zero.enqueue(result_one) if result_one.is_a?(Integer)
    one.enqueue(result_zero) if result_zero.is_a?(Integer)

    break if zero.q.empty? && one.q.empty? && [result_zero, result_one].all? { |r| %i[done waiting].include?(r) }
  end

  one.send_count
end

if __FILE__ == $0
  data = File.readlines('day_18_input.txt')
  p part_one(data)
  p part_two(data)
end
