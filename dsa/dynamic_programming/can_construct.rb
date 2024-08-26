def can_construct(target, word_bank)
  return true if target.empty?

  word_bank.each do |word|
    return true if target.start_with?(word) && can_construct(target.sub(word, ''), word_bank)
  end

  false
end

p can_construct('abcdef', %w[ab abc cd def abcd])
p can_construct('skateboard', %w[bo rd ate t ska sk boar])
p can_construct('', %w[a b c])
p can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', %w[eee ee e])
