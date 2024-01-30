#!/usr/bin/env ruby
#regex that matches
#+ prefix hb
#+ 2-5 occurrence(s) of t
#+ suffix n
puts ARGV[0].scan(/hbt{2,5}n/).join
