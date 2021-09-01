import random
class Authentifikator(object):
    def __init__(self):
        self.schlüssel = 0

        self.prime = 0
        self.other_number = 0
        self.secret_key = 0

        self.part1 = 0
        self.part1_partner = 0

        self.give_me_prime()
        self.create_my_number()
        self.create_other_number()

    def primesInRange(self,x, y):
        prime_list = []
        for n in range(x, y):
            isPrime = True

            for num in range(2, n):
                if n % num == 0:
                    isPrime = False
                    
            if isPrime:
                prime_list.append(n)
        return prime_list

    
    
    def give_me_prime(self):
        start = 1000
        stop = 2500
        prime_list = self.primesInRange(start,stop)
        randomPrime = random.choice(prime_list)
        self.prime = randomPrime

    def create_my_number(self):
        zahl = random.randint(1,self.prime-1)
        self.secret_key = zahl

    def create_other_number(self):
        zahl = random.randint(1,self.prime-1)
        self.other_number = zahl

    

    def diffy_part_1(self):
        Zahl = (self.other_number**self.secret_key)%self.prime
        self.part1 = Zahl

    def diffy_part2(self):
        Zahl = (self.part1_partner**self.secret_key)%self.prime
        print(Zahl)

    def set_prime(self,prime):
        self.prime = prime

    def set_other_number(self, number):
        self.other_number = number

    def set_part1(self,part1):
        self.part1_partner = part1

if __name__ == "__main__":
    Authy = Authentifikator()
    Authy_Client = Authentifikator()

    Authy_Client.set_prime(Authy.prime)
    Authy_Client.set_other_number(Authy.other_number)
    Authy_Client.create_my_number()

    Authy_Client.diffy_part_1()
    Authy.diffy_part_1()

    Authy.set_part1(Authy_Client.part1)
    Authy_Client.set_part1(Authy.part1)

    Authy.diffy_part2()
    Authy_Client.diffy_part2()


