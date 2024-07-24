# frozen_string_literal: true

def grid_traveler(x, y, memo = {})
  return memo[[x, y]] if memo[[x, y]]
  return 0 if x.zero? || y.zero?
  return 1 if x == 1 && y <= 1

  memo[[x, y]] = grid_traveler(x - 1, y, memo) + grid_traveler(x, y - 1, memo)
end

p grid_traveler(18, 18)
