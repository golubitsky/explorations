# part one and two
A_MULT_VALUE = 16_807
B_MULT_VALUE = 48_271
DIVIDE_VALUE = 2_147_483_647

# part two
A_MOD_CHECK = 4
B_MOD_CHECK = 8

def least_significant_16_bits(n)
  n & 0xFFFF # 2 ** 16
end

def gen_gen_part_one(start:, mult:)
  Enumerator.new do |yielder|
    n = start
    loop do
      n *= mult
      n %= DIVIDE_VALUE
      yielder << least_significant_16_bits(n)
    end
  end
end

def gen_gen_part_two(start:, mult:, mod_check:)
  Enumerator.new do |yielder|
    n = start
    loop do
      n *= mult
      n %= DIVIDE_VALUE
      yielder << least_significant_16_bits(n) if (n % mod_check).zero?
    end
  end
end

def part_one(a, b)
  gen_a = gen_gen_part_one(start: a, mult: A_MULT_VALUE)
  gen_b = gen_gen_part_one(start: b, mult: B_MULT_VALUE)

  count = 0

  40_000_000.times do |n|
    count += 1 if gen_a.next == gen_b.next
    p n if (n % 1_000_000).zero?
  end

  count
end

def part_two(a, b)
  gen_a = gen_gen_part_two(start: a, mult: A_MULT_VALUE, mod_check: A_MOD_CHECK)
  gen_b = gen_gen_part_two(start: b, mult: B_MULT_VALUE, mod_check: B_MOD_CHECK)

  count = 0

  5_000_000.times do
    count += 1 if gen_a.next == gen_b.next
  end

  count
end

if __FILE__ == $0
  # p part_one(65, 8921) # sample
  p part_one(591, 393)
  # p part_two(65, 8921) # sample
  p part_two(591, 393)
end
