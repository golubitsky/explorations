# frozen_string_literal: true

require 'json'

RSpec.describe HuffmanEncoding do
  let(:encoded) { HuffmanEncoding.encoded(string) }
  let(:decoded) { HuffmanEncoding.decoded(encoded) }

  context 'when simple string' do
    let(:string) { 'abc' }

    it 'encodes' do
      parsed_json = JSON.parse(encoded, symbolize_names: true)
      expect(parsed_json).to eq(
        {
          decoding_table: { '10': 'a', '11': 'b', '0': 'c' },
          encoded_string: '10110'
        }
      )
    end

    it 'decodes' do
      expect(decoded).to eq(string)
    end
  end
end
