#  verify if a number is prime

class Language:
    def __init__(self,number):
        self.number = number
    
    def compare(self,other_number):
        pass

def prime(x):
    if x < 2:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False

    return True

print(prime(1),
prime(2),
prime(4),
prime(9),
prime(7),
prime(32),
prime(59)
)
