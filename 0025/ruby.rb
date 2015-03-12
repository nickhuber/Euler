i = 1
answer = -1
previous = 0

while i.to_s.length < 1000
  answer += 1
  i, previous = previous, previous + i
end

puts answer