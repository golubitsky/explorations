# frozen_string_literal: true

def can_sum(target, integers, memo = {})
  return memo[target] if memo.key?(target)
  return true if target.zero?
  return false if target.negative?

  integers.any? do |integer|
    memo[target - integer] = can_sum(target - integer, integers, memo)
  end
end

def test_can_sum
  # Base Cases
  puts can_sum(0, [1, 2, 3]) == true          # target is zero
  puts can_sum(-5, [1, 2, 3]) == false        # target is negative
  puts can_sum(7, []) == false                # empty array of integers

  # General Cases
  puts can_sum(7, [2, 3]) == true             # 7 = 3 + 2 + 2
  puts can_sum(7, [5, 3, 4, 7]) == true       # 7 = 7
  puts can_sum(7, [2, 4]) == false            # No combination can sum to 7
  puts can_sum(8, [2, 3, 5]) == true          # 8 = 3 + 5

  # Edge Cases
  puts can_sum(300, [7, 14]) == false         # Large target with no combination
  puts can_sum(1, [2, 3, 5]) == false         # Small target with larger integers
  puts can_sum(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == true # Repeated integers
  puts can_sum(100, [1, 2, 5, 25]) == true # Combination using repeated and large integers
end

test_can_sum
