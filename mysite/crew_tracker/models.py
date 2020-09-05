from django.db import models


# Create your models here.
class ShipClass(models.Model):
    name = models.CharField(max_length=50)
    crew_requirement = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Starship(models.Model):
    name = models.CharField(max_length=50)
    ship_class = models.ForeignKey(ShipClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Crewman(models.Model):
    name = models.CharField(max_length=50)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    ship_assignment = models.ForeignKey(Starship, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name

