# frozen_string_literal: true

# best_sum encounteres stack level too deep (SystemStackError)
# this iterative solution solves that problem

def make_change(coins, amount)
  table = Array.new(amount + 1)
  table[0] = []

  (1..amount).each do |current_amount|
    coins.each do |coin|
      next unless current_amount >= coin
      next unless table[current_amount - coin]

      current = [*table[current_amount - coin], coin]
      table[current_amount] ||= current
      table[current_amount] = [current, table[current_amount]].min_by(&:length)
    end
  end

  table[amount]
end

p make_change([1], 10_000).count
