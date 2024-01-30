#!/usr/bin/env ruby
#regex that matches 10 digit num
puts ARGV[0].scan(/^\d{10,10}$/).join
