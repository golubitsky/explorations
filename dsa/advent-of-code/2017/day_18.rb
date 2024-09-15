PLAY_FREQUENCY = 'snd'
SET = 'set'
ADD = 'add'
MULTIPLY = 'mul'
REMAINDER = 'mod'
RECOVER_FREQUENCY = 'rcv'
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
  skip_count = 0
  registers = Hash.new(0)
  i = 0
  sound = nil

  while i < data.length
    instruction, register, raw_value = data[i].split
    value = parsed_value(raw_value, registers)

    case instruction
    when PLAY_FREQUENCY
      sound = registers[register]
    when SET
      registers[register] = value
    when ADD
      registers[register] += value
    when MULTIPLY
      registers[register] *= value
    when REMAINDER
      registers[register] %= value
    when RECOVER_FREQUENCY
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
  p registers
end

if __FILE__ == $0
  data = File.readlines('day_18_input.txt')
  p part_one(data)
end
