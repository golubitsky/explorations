# frozen_string_literal: true

def best_sum(target, integers, memo = {})
  return memo[target] if memo.key?(target)
  return [] if target.zero?
  return nil if target.negative?

  best_result = nil

  integers.each do |integer|
    result = best_sum(target - integer, integers, memo)

    next unless result

    result = [*result, integer]

    best_result = result if best_result.nil? || result.length < best_result.length
  end

  memo[target] = best_result
  best_result
end

# p best_sum(7, [5, 3, 4, 7]) == [7]
# p best_sum(8, [2, 3, 5]).sort == [3, 5].sort
# p best_sum(300, [7, 14])
# p best_sum(8, [3, 2])
p best_sum(11, [1, 2, 5])
p best_sum(8, [1, 4, 5])
p best_sum(100, [1, 2, 25])
p best_sum(10_000, [1]) # to solve for this , see make_change.rb
