prev = 0
cur = 1
sum = 0

while cur < 4000000 do
  if cur % 2 == 0
    sum += cur
  end
  tmp = cur
  cur = prev + cur
  prev = tmp
end

puts sum