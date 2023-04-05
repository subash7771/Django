from django.db import models

# Create your models here.
class Aprad(models.Model):
    code = models.IntegerField()
    village = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.village} ({self.code})"


class Samasya(models.Model):
    district = models.ForeignKey(Aprad, on_delete=models.CASCADE, related_name="Apradtype")
    address = models.ForeignKey(Aprad, on_delete=models.CASCADE, related_name="Apradreason")
    totalland = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.district} to {self.address}"
