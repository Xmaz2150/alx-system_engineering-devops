#!/usr/bin/env ruby
#regex that mathches str that starts with h
#+ ends with n
puts ARGV[0].scan(/^h.n$/).join
