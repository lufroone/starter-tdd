require 'answer'

RSpec.describe "answer" do
    it "gets the answer" do
        answer = get_answer()
        expect(answer).to eq 42
    end
end