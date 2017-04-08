import random
import math

random_numbers = list()

for x in range(50):
    random_numbers.append(random.randint(0, 49))

print('-----------random.randint()-----------')
print(random_numbers)
print('-----------random.choice()-----------')
print(random.choice(random_numbers))
print('-----------random.sample()-----------')
print(random.sample(random_numbers, 13))
print('-----------random.shuffle()-----------')
random.shuffle(random_numbers)
print(random_numbers)
print('-----------random.triangular()-----------')
dice_distribution = math.floor(random.triangular(2, 12, 7))
print('{}'.format(dice_distribution))
