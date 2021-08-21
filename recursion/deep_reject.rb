# frozen_string_literal: true

# Compare implementations with and without side effects.

def deep_reject(hash, &block)
  # Deeply rejects key/value pairs where the block returns true.
  # Also rejects key/value pairs whose nested contents are empty after rejection.
  hash.reduce({}) do |result, (key, value)|
    case value
    when String
      if block.call(key, value)
        # Don't add the key - reject it.
        result
      else
        result.merge(key => value)
      end
    when Hash
      nested_result = deep_reject(value, &block)
      # Also reject keys whose values are empty hashes
      nested_result.any? ? result.merge(key => nested_result) : result
    else
      raise 'expected deeply nested hash of hashes of strings'
    end
  end
end

def deep_reject!(hash, &block)
  hash.each do |key, value|
    case value
    when String
      hash.delete(key) if block.call(key, value)
    when Hash
      deep_reject!(value, &block)
      # Also reject keys whose values are empty hashes
      hash.delete(key) if value.empty?
    else
      raise 'expected deeply nested hash of hashes of strings'
    end
  end
end

def empty_hash
  {}
end

def shallow_hash_with_a
  { 'a' => '1' }
end

def hash
  { 'a' => '1', 'b' => '2', 'c' => '3', 'd' => { 'a' => '1' } }
end

REJECTOR = ->(k, _v) { k == 'a' }
