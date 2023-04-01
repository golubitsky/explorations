# frozen_string_literal: true

RSpec.describe HuffmanEncoding do
  let(:encoded) { HuffmanEncoding.encoded(string) }
  let(:decoded) { HuffmanEncoding.decoded(encoded) }

  context 'when simple string' do
    let(:string) { 'abc' }

    it 'encodes' do
      expect(encoded).to eq(
        {
          decoding_table: { '10' => 'a', '11' => 'b', '0' => 'c' },
          encoded_string: '10110'
        }
      )
    end

    it 'decodes' do
      expect(decoded).to eq(string)
    end
  end
end
