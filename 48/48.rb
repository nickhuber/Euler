total = 0
1.upto(1000) do |i|
  total += i**i 
end

p total.to_s.reverse.slice(0..9).reverse.to_i