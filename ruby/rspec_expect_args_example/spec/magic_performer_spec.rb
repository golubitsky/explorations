require 'rspec'
require_relative '../lib/magic_performer'

RSpec.describe MagicPerformer do
  let(:args_in_calls_to_do_magic) { [] }

  before do
    allow(Wrapper).to receive(:do_magic) do |*args, **kwargs|
      args_in_calls_to_do_magic << [args, kwargs]
    end

    MagicPerformer.new.perform_magic
  end

  it 'only calls the wrapper once with the correct arguments' do
    expect(args_in_calls_to_do_magic)
      .to eq([
               [[], { flowers_in_sleeve: false }]
             ])
  end
end
