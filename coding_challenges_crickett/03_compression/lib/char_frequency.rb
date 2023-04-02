# frozen_string_literal: true

module CharFrequency
  module_function

  def char_frequency_table(string)
    string.each_char.with_object(Hash.new(0)) do |char, table|
      table[char] += 1
    end
  end
end
