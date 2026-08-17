@'
#!/usr/bin/env ruby
match = ARGV.scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
puts match.join(,) if match.any?
'@
