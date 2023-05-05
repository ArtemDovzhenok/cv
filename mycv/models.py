from django.db import models
import random


class Comment(models.Model):
    author = models.CharField(max_length=30, verbose_name='Aвтop' )
    content = models.TextField(verbose_name='Coдepжaниe')
    email = models.EmailField(verbose_name='e-mail' )

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'





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

