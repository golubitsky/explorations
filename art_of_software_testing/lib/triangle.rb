# frozen_string_literal: true

def triangle(card)
  raise 'invalid input' unless valid_card?(card)

  {
    1 => 'equilateral',
    2 => 'isosceles',
    3 => 'scalene'
  }[card.uniq.count]
end

def valid_card?(card)
  exactly_three_sides?(card) &&
    only_integers?(card) &&
    all_sides_positive?(card) &&
    passes_triangle_inequality_theorem?(card)
end

def exactly_three_sides?(card)
  card.count == 3
end

def only_integers?(card)
  card.all? { |side| side.is_a?(Integer) }
end

def all_sides_positive?(card)
  card.all?(&:positive?)
end

def passes_triangle_inequality_theorem?(card)
  a, b, c = card
  a + b > c && a + c > b && b + c > a
end
