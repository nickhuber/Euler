$h = Hash.new

def sequence(number)
  i = 0
  until number == 1
    if $h.has_key?(number)
      return i + $h[number]
    end
    
    if number.even?
      number = number / 2
    else
      number = number * 3 + 1
    end
    i += 1
  end
  
  return i + 1
end

longest, amount = 0, 0

(1..1_000_000).each do |i|
  $h[i] = sequence(i)
  longest, amount = i, $h[i] if $h[i] > amount
end

p longest