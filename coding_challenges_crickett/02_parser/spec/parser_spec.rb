# frozen_string_literal: true

require 'open3'

require 'spec_helper'

RSpec.describe 'parsing JSON' do
  subject(:result) do
    _stdin, stdout, stderr, wait_thr = Open3.popen3(command)

    {
      stdout: stdout.read,
      stderr: stderr.read,
      exit_code: wait_thr.value.exitstatus
    }
  end

  describe 'step 1' do
    context 'when valid JSON' do
      let(:command) { 'ruby parser.rb spec/data/step1/valid.json' }

      it 'prints to stdout that input is valid JSON' do
        expect(result[:stdout]).to eq("spec/data/step1/valid.json is valid JSON\n")
      end

      it 'does not print to stderr' do
        expect(result[:stderr]).to eq('')
      end

      it 'exits 0' do
        expect(result[:exit_code]).to eq(0)
      end
    end

    context 'when invalid JSON' do
      let(:command) { 'ruby parser.rb spec/data/step1/invalid.json' }

      it 'prints to stdout that input is invalid JSON' do
        expect(result[:stdout]).to eq("spec/data/step1/invalid.json is invalid JSON\n")
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
