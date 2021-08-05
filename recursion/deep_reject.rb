# frozen_string_literal: true

def deep_reject(hash, &block)
  # Deeply rejects key/value pairs where the block returns true.
  # Also rejects key/value pairs whose nested contents are empty after rejection.
  hash.reduce({}) do |result, (key, value)|
    case value
    when Hash
      nested_result = deep_reject(value, &block)
      # Also reject keys whose values are empty hashes
      nested_result.any? ? result.merge(key => nested_result) : result
    when String
      if block.call(key, value)
        # Don't add the key - reject it.
        result
      else
        result.merge(key => value)
      end
    else
      raise 'expected deeply nested hash of hashes of strings'
    end
  end
end

pp deep_reject({}) { |k| k == 'a' } # => {}
pp deep_reject({ 'a' => '1' }) { |k| k == 'a' } # => {}

hash = { 'a' => '1', 'b' => '2', 'c' => '3', 'd' => { 'a' => '1' } }
pp deep_reject(hash) { |k| k == 'a' } # => {"b"=>"2", "c"=>"3"}
