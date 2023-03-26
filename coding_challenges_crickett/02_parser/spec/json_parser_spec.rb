# frozen_string_literal: true

require 'open3'

require 'spec_helper'

RSpec.shared_examples 'parses JSON' do
  subject(:result) do
    _stdin, stdout, stderr, wait_thr = Open3.popen3(command)

    {
      stdout: stdout.read,
      stderr: stderr.read,
      exit_code: wait_thr.value.exitstatus
    }
  end

  [
    'spec/data/step1/valid.json',
    'spec/data/step2/valid.json',
    'spec/data/step2/valid2.json',
    'spec/data/step3/valid.json',
    'spec/data/step4/valid.json',
    'spec/data/step4/valid2.json'
  ].each do |path_to_valid_file|
    context "when valid JSON #{path_to_valid_file}" do
      let(:file_path) { path_to_valid_file }

      it 'prints to stdout that input is valid JSON' do
        expect(result[:stdout]).to eq("#{path_to_valid_file} is valid JSON\n")
      end

      it 'does not print to stderr' do
        expect(result[:stderr]).to eq('')
      end

      it 'exits 0' do
        expect(result[:exit_code]).to eq(0)
      end
    end
  end

  [
    'spec/data/step1/invalid.json',
    'spec/data/step2/invalid.json',
    'spec/data/step2/invalid2.json',
    'spec/data/step3/invalid.json',
    'spec/data/step4/invalid.json'
  ].each do |path_to_invalid_file|
    context "when invalid JSON #{path_to_invalid_file}" do
      let(:file_path) { path_to_invalid_file }

      it 'prints to stdout that input is invalid JSON' do
        expect(result[:stdout]).to eq("#{file_path} is invalid JSON\n")
      end

      it 'does not print to stderr' do
        expect(result[:stderr]).to eq('')
      end

      it 'exits 0' do
        expect(result[:exit_code]).to eq(1)
      end
    end
  end
end

RSpec.describe 'parsing JSON' do
  context 'when implemented in Ruby' do
    let(:command) { "ruby json_parser.rb #{file_path}" }

    include_examples 'parses JSON'
  end

  context 'when implemented in Python' do
    let(:command) { "python3 json_parser.py #{file_path}" }

    include_examples 'parses JSON'
  end
end