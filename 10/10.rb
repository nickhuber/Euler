require 'mathn'

total = 0

Prime.instance.each(2_000_000) do |prime|
  total += prime
end

p total