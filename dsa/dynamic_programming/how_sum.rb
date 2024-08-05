# frozen_string_literal: true

def how_sum(target, integers, path_so_far = [], memo = {})
  if memo.key?(target)
    return memo[target]
  elsif target.zero?
    return path_so_far.any? ? path_so_far : false
  elsif target.negative?
    return false
  end

  integers.each do |integer|
    next_target = target - integer
    next_path = path_so_far.dup.push(integer)
    path = how_sum(next_target, integers, next_path, memo)

    return memo[target] = path if path
  end

  memo[target] = false
end

def test_how_sum
  # Base Cases
  p how_sum(0, [1, 2, 3]) # target is zero
  p how_sum(-5, [1, 2, 3])        # target is negative
  p how_sum(7, [])                # empty array of integers

  # # General Cases
  p how_sum(7, [2, 3]) # 7 = 3 + 2 + 2
  p how_sum(7, [5, 3, 4, 7]) # 7 = 7 or 3,4
  p how_sum(7, [2, 4]) # No combination can sum to 7
  p how_sum(8, [2, 3, 5]) # 8 = 3 + 5 or 2,2,2,2

  # # Edge Cases
  p how_sum(300, [7, 14]) # Large target with no combination
  p how_sum(1, [2, 3, 5]) # Small target with larger integers
  p how_sum(10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # Repeated integers
  p how_sum(100, [1, 2, 5, 25]) # Combination using repeated and large integers
  p how_sum(122, [98, 24, 1]) # multiple combinations, unsorted
end

test_how_sum
