# frozen_string_literal: true

def fib(n, memo = {})
  return memo[n] if memo[n]
  return 1 if n <= 2

  memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
end

p fib(10)
