import random
from typing import Union

def main() -> Union[bool, int]:
    
    a = random.randint(0, 100)
    b = random.randint(100, 142)
    c = (a+b)//(a**(b-a**(b*a)))