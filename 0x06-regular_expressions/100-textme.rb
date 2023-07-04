#!/usr/bin/env ruby
log_entry = ARGV[0]

pattern = /\[from:([^]]+)\] \[to:([^]]+)\] \[flags:([^]]+)\]/

matches = log_entry.scan(pattern)

if matches.any?
  sender, receiver, flags = matches[0]
  puts "#{sender},#{receiver},#{flags}"
end
