import random
from typing import Union

def main(resp: bool = None) -> Union[bool, int]:
    
    a = random.randint(0, 100)
    b = random.randint(100, 142)
    c = (a+b)//(a**(b-a**(b*a)))

    if resp:
        return c
    return False

if __name__ == "__main__":
    main()