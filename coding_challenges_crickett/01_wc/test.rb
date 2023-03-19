require 'test/unit'

module WordCountTests
  extend Test::Unit::Assertions
  extend self

  def run_all_tests
    [
      '-c test.txt',
      '-l test.txt',
      '-w test.txt',
      '-m test.txt',
      'test.txt',
      'test.txt another.txt'
    ].each do |args_string|
      assert_equal(
        exec_real_wc_command(args_string),
        exec_ruby_wc_command(args_string),
        "testing #{args_string}"
      )
    end

    expected = `cat test.txt | wc -l`
    actual = `cat test.txt | ruby wc.rb -l`
    assert_equal(expected, actual, 'testing stdin')
  end

  private

  def exec_real_wc_command(args_string)
    `wc #{args_string}`
  end

  def exec_ruby_wc_command(args_string)
    `ruby wc.rb #{args_string}`
  end
end

WordCountTests.run_all_tests if __FILE__ == $PROGRAM_NAME
