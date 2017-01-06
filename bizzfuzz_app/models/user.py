from django.db import models
from random import randint
from datetime import date


def random_number_generate():
    return randint(1, 100)


class User(models.Model):
    name = models.CharField(max_length=40, null=True)
    birthday = models.DateField(null=False, default="1970-01-01")
    number = models.IntegerField(default=random_number_generate)

    def get_eligibility(self):
        # Calculate age
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

        return "allowed" if age > 13 else "blocked"

    def get_bizzfuzz(self):
        number = self.number

        if number % 3 == 0 and number % 5 == 0:
            result = "BizzFuzz"
        elif number % 3 == 0:
            result = "Bizz"
        elif number % 5 == 0:
            result = "Fuzz"
        else:
            result = number

        return result
