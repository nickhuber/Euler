def palindrome?(string)
  string.reverse == string
end

results = Array.new

1.upto(1_000_000) do |i|
  results.push(i) if palindrome?(i.to_s) and palindrome?(i.to_s(2))
end

p results.inject(:+)