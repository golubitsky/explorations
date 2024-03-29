require 'csv'

def ask_question(problem, index)
  print "Problem #{index + 1}: #{problem[:question]} = "
  user_answer = gets.chomp

  user_answer == problem[:answer]
end

def quiz(problems)
  result = 0

  problems.each_with_index do |problem, index|
    result += 1 if ask_question(problem, index)
  end
ensure
  puts "\nYou scored #{result} out of #{problems.count}"
end

def timer(seconds)
  sleep(seconds)
end

problems = CSV.readlines('problems.csv').map do |line|
  {
    question: line.first,
    answer: line.last
  }
end

quiz_thread = Thread.new { quiz(problems) }

timer(5)

quiz_thread.kill
