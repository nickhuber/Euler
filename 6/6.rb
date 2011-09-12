sum_of_squares = 0
for i in 1..100 
  sum_of_squares += i * i
end

sums = 0
for i in 1..100 
  sums += i
end

square_of_sums = sums * sums

puts square_of_sums - sum_of_squares