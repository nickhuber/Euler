require 'mathn'

num = 317_584_931_803
factor = 0
primes = Prime.new

while num > 1
  factor = primes.next
  num /= factor while (num % factor).zero? #divide out all the times this prime divides
end
 
p factor