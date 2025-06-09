
#direct complete importing

# import random
# coin = random.choice(["heads", "tails"])
# print(coin)

# importing just some that makes us use only one of it

# from random import choice
# coin = choice(["heads","tails"])
# print(coin)

import random
coin = random.choice(["heads", "tails"])
print(coin)

#choosing random number from 1 to 10
number = random.randint(1,10)
print (number)

#shuffle the list 
card = ["jack", "queen", "king", "A"]
random.shuffle(card)
print(card)

#statistics
import statistics
mean = statistics.mean([1,2,3,4,5])
print(mean)