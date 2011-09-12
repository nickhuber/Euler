found = false
num = 0
while (!found)
  num += 20
  for i in 1..20
    if num % i != 0
      break
    end
    found = true if i == 20
  end
end
puts num