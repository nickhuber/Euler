require 'mathn'

primes = Prime.each
prime = 0

10_001.times do
  prime = primes.next
end

p prime