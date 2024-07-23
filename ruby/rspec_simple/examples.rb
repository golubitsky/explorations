describe 'special y feature' do
  context 'when feature flag on' do
    let(:feature_flag) { on }

    context 'when data of type x' do
      let(:data) { 'x' }

      it 'processes the data'
    end

    context 'when data of type y' do
      let(:data) { 'y' }

      it 'processes the data in a special way'
    end
  end

  context 'when feature flag off' do
    let(:feature_flag) { off }

    context 'when data of type x' do
      let(:data) { 'x' }

      it 'processes the data'
    end

    context 'when data of type y' do
      let(:data) { 'y' }

      it 'processes the data'
    end
  end
end
