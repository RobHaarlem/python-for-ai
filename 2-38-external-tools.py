# Import Patterns Explained

# import a whole module
import math
#Now use:math.sqrt(16)
print(math.sqrt(16))

# import specific items from a module
from math import sqrt, pi
#Now use sqrt(16)
print(sqrt(16))

import random
#Use module functions
number = random.randint(1,10)
print(number)
choice = random.choice(["apple", "bannana", "orange", "strawberry"])
print(choice)

import numpy as np
import pandas as pd