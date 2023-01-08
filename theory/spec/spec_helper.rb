# frozen_string_literal: true

Dir['..lib/**/*.rb'].sort.each { |file| require_relative file }

RSpec.configure do |c|
  c.filter_run_when_matching focus: true
end
