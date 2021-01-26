require 'test/unit'
require 'rspec'
require 'rspec/autorun'
require './src/main/java/durr_vie/CharacterStrings/Anagrams/anagrams.rb'

=begin
RSpec.describe 'anagrams' do
  describe '#some_method_under_test' do
    subject { anagrams input }

    [
      ["below the car is a rat drinking cider and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel", [
     ['bowel', 'below', 'elbow'], ['arc', 'car'], ['night', 'thing'], ['cried', 'cider'], ['act', 'cat']]]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        # let(:input_value) { input }
        actual_result = anagrams(input)
        expect(anagrams(input)).to eql expected_output
        expect(actual_result).to equal(expected_output)
        expect(actual_result).to be == expected_output
      end
    end
  end
end
=end
