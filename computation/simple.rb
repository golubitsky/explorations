# frozen_string_literal: true

module ReducibleOperator
  def redicible?
    true
  end

  def reduce
    if left.redicible?
      self.class.new(left.reduce, right)
    elsif right.reducible?
      self.class.new(left, right.reduce)
    else
      Number.new(left.value + right.value)
    end
  end
end

Number = Struct.new(:value) do
  def to_s
    value.to_s
  end

  def inspect
    "<#{self}>"
  end

  def redicible?
    false
  end
end

Add = Struct.new(:left, :right) do
  include ReducibleOperator

  def to_s
    "#{left} + #{right}"
  end

  def inspect
    "<#{self}>"
  end
end

Multiply = Struct.new(:left, :right) do
  include ReducibleOperator

  def to_s
    "#{left} * #{right}"
  end

  def inspect
    "<#{self}>"
  end
end

def main
  p Add.new(
    Multiply.new(Number.new(1), Number.new(2)),
    Multiply.new(Number.new(3), Number.new(4))
  )
  p Number.new(5)
end

main if $PROGRAM_NAME == __FILE__
