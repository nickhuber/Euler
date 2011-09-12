puts (1..999).select { |i| x % 3 == 0 || x % 5 == 0 }.reduce(:+)
