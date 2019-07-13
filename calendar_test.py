import random
import string
import crypt
randomsalt = ''.join(random.sample(string.ascii_letters, 8))
randomsalt = '$6$' + randomsalt + '$'
print(randomsalt)

p = crypt.crypt('password', randomsalt)
print(p)
