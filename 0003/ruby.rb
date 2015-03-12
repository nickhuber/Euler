require 'mathn'

num = 600_851_475_143
factor = 0
primes = Prime.each

while num > 1
  factor = primes.next
  num /= factor while (num % factor).zero? #divide out all the times this prime divides
end
 
p factor