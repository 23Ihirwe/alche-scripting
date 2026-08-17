#!/usr/bin/env ruby
input = ARGV[0]
m = input.match(/from:([^]]+).*to:([^]]+).*flags:([^]]+)/)
puts "#{m[1]},#{m[2]},#{m[3]}" if m
