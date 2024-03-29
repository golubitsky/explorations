# frozen_string_literal: true

require 'open3'

require 'spec_helper'

RSpec.describe 'compression' do
  let(:encode) do
    _stdin, stdout, stderr, wait_thr = Open3.popen3(encode_command)

    {
      stdout: stdout.read,
      stderr: stderr.read,
      exit_code: wait_thr.value.exitstatus
    }
  end

  let(:decode) do
    _stdin, stdout, stderr, wait_thr = Open3.popen3(decode_command)

    {
      stdout: stdout.read,
      stderr: stderr.read,
      exit_code: wait_thr.value.exitstatus
    }
  end

  let(:file_path) { 'spec/data/135-0.txt' }
  let(:encoded_file_path) { 'spec/data/135-0.txt-encoded' }
  let(:decoding_table_file_path) { 'spec/data/135-0.txt-table' }
  let(:decoded_file_path) { 'spec/data/135-0.txt-encoded-decoded' }
  let(:expected_decoded_result) { File.read(file_path) }
  let(:actual_encoded_result) { File.read(encoded_file_path) }
  let(:actual_decoded_result) { File.read(decoded_file_path) }

  let(:encode_command) { "ruby compression.rb --encode #{file_path}" }
  let(:decode_command) do
    "ruby compression.rb --decode #{encoded_file_path} #{decoding_table_file_path}"
  end

  before do
    encode
    decode
  end

  after do
    FileUtils.rm_f(encoded_file_path)
    FileUtils.rm_f(decoding_table_file_path)
    FileUtils.rm_f(decoded_file_path)
  end

  it 'encodes and compresses the file to almost to half the file size',
     :aggregate_failures do
    expected_stdout = [
      "encoded spec/data/135-0.txt to spec/data/135-0.txt-encoded\n",
      "stored decoding table at spec/data/135-0.txt-table\n"
    ]
    expect(encode[:stdout]).to eq(expected_stdout.join)
    expect(encode[:stderr]).to eq('')
    expect(encode[:exit_code]).to eq(0)

    expect(File).to exist(encoded_file_path)
    percent_of_file_size_compressed =
      1 - (File.size('spec/data/135-0.txt-encoded').to_f / File.size('spec/data/135-0.txt'))
    expect(percent_of_file_size_compressed).to be > 0.43
  end

  it 'decodes the encoded/compressed file to original', :aggregate_failures do
    expect(decode[:stdout]).to eq("decoded spec/data/135-0.txt-encoded to spec/data/135-0.txt-encoded-decoded\n")
    expect(decode[:stderr]).to eq('')
    expect(decode[:exit_code]).to eq(0)

    # sanity check that encoded is different from decoded
    expect(actual_encoded_result).not_to eq(expected_decoded_result)

    expect(actual_decoded_result).to eq(expected_decoded_result)
  end
end
