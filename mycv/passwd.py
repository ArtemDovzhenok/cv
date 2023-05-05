import random

class genericPWD:
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    def __init__(self, number, length):
        self.number = int(number)
        self.length = int(length)

    def layoutpwd(self):
        output = []
        for n in range(self.number):
            password =''
            for i in range(self.length):
                password += random.choice(self.chars)
            output.append(password)
        return  output
