task default: %w[test]

task :test do
#   ruby 'test/unittest.rb'
end

$LOAD_PATH.unshift(File.dirname(__FILE__) + '/../../lib')
require 'cucumber/rake/task'

Cucumber::Rake::Task.new do |t|
  t.cucumber_opts = %w[--format pretty]
end