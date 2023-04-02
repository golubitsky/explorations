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

  context 'when Les Miserables' do
    let(:string) { File.read('spec/data/135-0.txt')[0..5_000] }

    specify 'encoded + decoded == original' do
      expect(decoded).to eq(string)
    end

    specify 'encoded string is compressed' do
      fail_message = 'expected encoded to be compressed: ' \
                     "encoded is length #{encoded.length}, " \
                     "while input was #{string.length}"
      expect(encoded.length).to be < string.length, fail_message
    end
  end

  describe 'unique character limits' do
    context 'when 128 unique chars' do
      let(:string) { [*0..127].map(&:chr).join }

      it 'it works' do
        expect { encoded }.not_to raise_error
      end
    end

    context 'when more than 128 unique chars' do
      let(:string) { [*0..128].map(&:chr).join }

      it 'is not implemented' do
        expect { encoded }.to raise_error(
          /encoding more than 128 unique characters is not supported/
        )
      end
    end
  end
end
