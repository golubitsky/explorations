class Wrapper
  def self.do_magic(options = {})
    # implementation goes here
  end
end

class MagicPerformer
  def perform_magic
    Wrapper.do_magic(flowers_in_sleeve: false)
  end
end