import random

HEADS = 0
TAILS = 1
RAND = 10
GAMES = 1000000

heads = 0

for i in range(0, GAMES):
    coin = HEADS

    if random.randint(0, RAND) % 2:
        coin = random.randint(0, RAND) % 2
    
    if random.randint(0, RAND) % 2:
        coin = random.randint(0, RAND) % 2

    if random.randint(0, RAND) % 2:
        coin = random.randint(0, RAND) % 2

    if random.randint(0, RAND) % 2:
        coin = random.randint(0, RAND) % 2

    if coin == HEADS:
        heads += 1

print("Heads %d out of %d games\n" % (heads, GAMES))