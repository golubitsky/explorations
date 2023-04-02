# frozen_string_literal: true

require 'open3'

require 'spec_helper'

RSpec.describe 'compression' do
  context 'when valid input' do
    let(:encode) do
      _stdin, stdout, stderr, wait_thr = Open3.popen3("ruby compression.rb --encode #{file_path}")

      {
        stdout: stdout.read,
        stderr: stderr.read,
        exit_code: wait_thr.value.exitstatus
      }
    end

    let(:decode) do
      _stdin, stdout, stderr, wait_thr = Open3.popen3("ruby compression.rb --decode #{encoded_file_path}")

      {
        stdout: stdout.read,
        stderr: stderr.read,
        exit_code: wait_thr.value.exitstatus
      }
    end

    let(:file_path) { 'spec/data/135-0.txt' }
    let(:encoded_file_path) { 'spec/data/135-0.txt-encoded' }
    let(:expected_decoded_result) { File.read('spec/data/135-0.txt') }

    describe 'encoding' do
      before do
        encode
        decode
      end

      after do
        FileUtils.rm_f(encoded_file_path)
      end

      fit 'encodes the file' do
        expect(encode[:stdout]).to eq("encoded spec/data/135-0.txt to spec/data/135-0.txt-encoded\n")
        expect(File).to exist(encoded_file_path)
      end

      fit 'does not print to stderr' do
        expect(encode[:stderr]).to eq('')
      end

      it 'exits 0' do
        expect(encode[:exit_code]).to eq(0)
      end
    end

    describe 'decoding the encoded file' do
      before do
        encode
        decode
      end

      after do
        FileUtils.rm_f(encoded_file_path)
      end

      it 'encodes the file' do
        expect(decode[:stdout]).to eq("encoded spec/data/135-0.txt to spec/data/135-0.txt-encoded\n")
      end

      it 'does not print to stderr' do
        expect(decode[:stderr]).to eq('')
      end

      it 'exits 0' do
        expect(decode[:exit_code]).to eq(0)
      end
    end
  end
end
