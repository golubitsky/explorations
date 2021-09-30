# frozen_string_literal: true

class ClassyHuman
  def initialize(name)
    @name = name
  end

  def say_hello
    puts "Hi, my name is #{@name}"
  end
end

def human_via_closure(name); end

def say_hello; end

ClassyHuman.new('Fred').say_hello
