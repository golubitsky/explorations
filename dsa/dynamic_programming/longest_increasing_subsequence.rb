# frozen_string_literal: true

def subsets(numbers)
  return [[]] if numbers.empty?

  inner = subsets(numbers[0..-2])

  inner + inner.map { |seq| [*seq, numbers.last] }
end

def brute_force(numbers)
  subsets(numbers)
    .select { |x| x == x.sort && x.uniq.count == x.length }
    .max_by(&:length)
end

p brute_force([0, 1, 0, 3, 2, 3])
