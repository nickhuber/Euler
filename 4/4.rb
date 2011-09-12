def palindrome?(string)
  string.reverse == string
end

biggest = 0

for i in 100..999
  for j in 100..999
    if palindrome?((i * j).to_s)
      biggest = i * j if biggest < i * j
    end
  end
end

p biggest