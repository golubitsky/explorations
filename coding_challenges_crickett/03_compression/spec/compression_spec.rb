# frozen_string_literal: true

require 'open3'

require 'spec_helper'

RSpec.describe 'compression' do
  subject(:result) do
    _stdin, stdout, stderr, wait_thr = Open3.popen3("ruby compression.rb #{file_path}")

    {
      stdout: stdout.read,
      stderr: stderr.read,
      exit_code: wait_thr.value.exitstatus
    }
  end

  context 'when valid input' do
    let(:file_path) { 'spec/data/135-0.txt' }

    it 'prints to stdout that input is valid JSON' do
      expect(result[:stdout]).to eq('')
    end

    it 'does not print to stderr' do
      expect(result[:stderr]).to eq('')
    end

    it 'exits 0' do
      expect(result[:exit_code]).to eq(0)
    end
  end
end
