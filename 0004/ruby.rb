def palindrome?(string)
  string.reverse == string
end

max = 0

for i in 100..999
  for j in 100..999
    if palindrome?((i * j).to_s)
      max = [max, i * j].max
    end
  end
end

p max