# frozen_string_literal: true

# rubocop:disable Metrics/BlockLength
RSpec.describe 'A Self-Assessment Test' do
  describe 'identification of triangles' do
    [
      [[1, 1, 1], 'equilateral'],
      # any order isosceles
      [[2, 2, 1], 'isosceles'],
      [[2, 1, 2], 'isosceles'],
      [[1, 2, 2], 'isosceles'],
      # any order scalene
      [[3, 4, 5], 'scalene'],
      [[3, 5, 4], 'scalene'],
      [[4, 3, 5], 'scalene'],
      [[4, 5, 3], 'scalene'],
      [[5, 4, 3], 'scalene'],
      [[5, 3, 4], 'scalene']
    ].each do |(card, triangle_type)|
      it "identifies #{card.join(', ')} as #{triangle_type}" do
        expect(triangle_type(card)).to eq(triangle_type)
      end
    end
  end

  describe 'detection of non-triangles' do
    [
      # negative side
      [-1, 1, 1],
      [1, -1, 1],
      [1, 1, -1],
      # zero side
      [0, 2, 2],
      [2, 0, 2],
      [2, 2, 0],
      # all zero sides
      [0, 0, 0],
      # breaks triangle inequality theorem; sum of 2 sides equals 3rd
      [2, 1, 1],
      [1, 2, 1],
      [1, 1, 2],
      # breaks triangle inequality theorem; sum of 2 sides less than 3rd
      [100, 7, 11],
      [7, 100, 11],
      [7, 11, 100],
      # only accepts integers (even if triangle is otherwise valid)
      %w[1 1 1],
      # too many or too few values
      [],
      [1, 1],
      [1, 1, 1, 1]
    ].each do |card_with_non_triangle|
      it "rejects invalid input #{card_with_non_triangle.inspect}" do
        expect { triangle_type(card_with_non_triangle) }.to raise_error('invalid input')
      end
    end
  end
end
# rubocop:enable Metrics/BlockLength
