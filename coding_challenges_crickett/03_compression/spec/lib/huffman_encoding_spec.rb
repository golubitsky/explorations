# frozen_string_literal: true

RSpec.describe HuffmanEncoding do
  let(:encoded) { described_class.encoded(string) }
  let(:binary_string) { encoded[:binary_string] }
  let(:decoding_table) do
    eval(encoded[:utf_8_json_decoding_table_hash_as_string])
  end
  let(:decoded) { described_class.decoded(**encoded) }

  context 'when simple string' do
    let(:string) { 'abc' }

    it 'encodes the string as an integer' do
      expect(binary_string).to eq('10110')
    end

    it 'returns a decoding table in UTF-8' do
      expect(decoding_table).to eq({ '10' => 'a', '11' => 'b', '0' => 'c' })
    end

    it 'decodes' do
      expect(decoded).to eq(string)
    end
  end

  context 'when string with spaces' do
    let(:string) { 'ab cde' }

    it 'decodes' do
      expect(decoded).to eq(string)
    end
  end

  context 'when Les Miserables' do
    let(:string) { File.read('spec/data/135-0.txt') }

    specify 'encoded + decoded == original' do
      expect(decoded).to eq(string)
    end
  end

  describe 'unique character limits (TODO: not sure if this limit is needed anymore)' do
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
