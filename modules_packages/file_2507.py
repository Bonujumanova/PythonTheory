import math
import random
from random import randint

random.randint(5, 15)
randint(4, 10)

# ---------------------------

import utils
from modules_packages.utils import print_nums
from .utils import print_nums

print_nums()
utils.print_nums()

# ---------------------------

from modules_packages.mathematic.trigonometry import contants as trio_const
from modules_packages.mathematic.geometrey import contants as geo_const
import modules_packages.mathematic as mpm

print(trio_const.PI)
print(trio_const.e)

# mpm.trigonometry.PI
print(mpm.PI)
